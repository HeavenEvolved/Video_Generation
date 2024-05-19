# ##### nvitop #####

# from nvitop import Device

##### Flask Imports #####

import os
from flask import Flask, render_template, request, redirect, url_for
from flask_cors import cross_origin, CORS

##### Wav2Lip Imports #####

from lipsync import lipsync

##### Voice Clone Imports #####

from cloner import cloner

##### TTS Imports #####

from TTS.api import TTS

app = Flask(__name__, static_folder='./static', template_folder='./templates')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["TEMPLATES_AUTO_RELOAD"] = True

tts_out_path = os.getcwd()+'/static/output.wav'

# devices = Device.cuda.all()

# if devices:

#     for device in devices:
#         processes = device.processes()
#         sorted_pids = sorted(processes)

#         print('\n', device, '\n')
#         print(f'  - Fan speed:       {device.fan_speed()}%')
#         print(f'  - Temperature:     {device.temperature()}C')
#         print(f'  - GPU utilization: {device.gpu_utilization()}%')
#         print(f'  - Total memory:    {device.memory_total_human()}')
#         print(f'  - Used memory:     {device.memory_used_human()}')
#         print(f'  - Free memory:     {device.memory_free_human()}')
#         print(f'  - Processes ({len(processes)}): {sorted_pids}')

#         for pid in sorted_pids:
#             print(f'    - {processes[pid]}')
#         print('-' * 120)

model = TTS.list_models(TTS())[0]
tts = TTS(model, progress_bar=True)
del model
speakers = [x.strip() for x in tts.speakers if 'en' in x]
languages = [x.strip() for x in tts.languages]

@app.route("/tts", methods=['POST'])
def ttshandler():
    
    if request.method == 'POST':

        try:

            if request.form['choice'] == 'main':
                return redirect('main.html')
            elif request.form['choice'] == 'previous':
                return redirect(request.referrer)
            
        except:

            pass
        
        speaker = request.form['speaker']
        sentence = request.form['sentence']
        language = request.form['language']

        try:

            video = request.files['video_file'].read()

            with open('./static/input_video.mp4', 'wb') as fp:

                fp.write(video)

            video = os.getcwd() + './static/input_video.mp4'

        except:
            
            video = os.getcwd()+"/static/"+[x for x in os.listdir(os.getcwd()+"/static/") if 'sample.' in x][0]
        
        tts.tts_to_file(text=sentence, speaker=speaker, language=language, file_path=tts_out_path)
        print()        
        print(video)
        print()
        lipsync(video)

    return "TTS Completed"

@app.route("/clone", methods=['POST'])
def clonerhandler():
    
    if request.method == 'POST':

        try:

            if request.form['choice'] == 'main':
                return redirect('main.html')
            elif request.form['choice'] == 'previous':
                return redirect(request.referrer)
            
        except:

            pass
        
        audiofile = request.files['file'].read()
        sentence = request.form['sentence']
        
        print(sentence)
        
        with open('./static/recorded_audio.wav', 'wb') as fp:
            
            fp.write(audiofile)

        try:

            video = request.files['video_file'].read()

            with open('./static/input_video.mp4', 'wb') as fp:

                fp.write(video)

            video = os.getcwd() + './static/input_video.mp4'

        except:

            video = os.getcwd()+"/static/sample_video.mp4"

        cloner(sentence)
        print()
        lipsync(video)

    return "Cloning Completed"

@app.route("/", methods=['GET', 'POST'])
def main():

    request_type = request.method

    if request_type == 'GET':

        return render_template('main.html')

    elif request_type == 'POST':

        choice = request.form['choice']
        
        if choice == 'clone':
            return render_template('clone.html')
        elif choice == 'tts':
            return render_template('tts.html', speakers=sorted(list(set(speakers))), languages=languages)
    
if __name__ == "__main__":
    app.run(debug=True)