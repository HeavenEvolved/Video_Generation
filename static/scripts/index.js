//vars

var startRecordingButton = document.getElementsByClassName("startRecordingButton")[0];
var stopRecordingButton = document.getElementsByClassName("stopRecordingButton")[0];
var recordingDot = document.getElementsByClassName("dot")[0];
var audioElement = document.getElementsByClassName("audio-element")[0];
var audioElementSource = document.getElementsByClassName("audio-element")[0].getElementsByTagName("source")[0];

var sentence = document.getElementById("sentence");

//listeners

startRecordingButton.onclick = startAudioRecording;
stopRecordingButton.onclick = stopAudioRecording;

function mainMenu()    {

    var xmlhttp = new XMLHttpRequest();

    var fd = new FormData();

    fd.set('choice', 'main');

    xmlhttp.onload = function() {

        console.log(this.response);

    }

    var url = '/clone';

    xmlhttp.open("POST", url, true);
    xmlhttp.send(fd);

}

function previousMenu() {

    location.reload();

}

function startAudioRecording()  {

    console.log("Started Recording Audio!");

    stopRecordingButton.disabled = false;

    recordingDot.style.visibility = "visible";

    audioRecorder.start();

}

function stopAudioRecording()   {

    console.log("Stopped Recording!");

    recordingDot.style.display = "none";

    audioRecorder.stop()
        .then(audioAsBlob => {

            playAudio(audioAsBlob);

            var xmlhttp = new XMLHttpRequest();

            var fd = new FormData();
            fd.set('file', audioAsBlob, 'recorded_audio.wav');

            console.log("Sentence: "+ sentence.value);

            fd.set('sentence', sentence.value);
            var url = "/clone";

            if(hasFile) {
                fd.set('video_file', file, 'input_video.' + file['type'].substring(("video/").length,));
            }

            xmlhttp.onload = function() {

                console.log(this.response);

                var main = document.getElementsByClassName("main")[0];

                main.style.display = "none";

                var player = document.getElementById("player");

                player.load();
        
                var video = document.getElementsByClassName("video")[0];
        
                video.style.display = "flex";

                player.play();

            }

            xmlhttp.open("POST", url, true);
            xmlhttp.send(fd);

        })

}

var file;

var hasFile = false;

function validateAndUpload(input)   {

    file = input.files[0];

    if(file)
        hasFile = true;

    console.log(file['type'].substring(("video/").length,));

}

//helper function
function createSourceForAudioElement() {
    let sourceElement = document.createElement("source");
    audioElement.appendChild(sourceElement);

    audioElementSource = sourceElement;
}

function playAudio(recordedBlob)    {

    let reader = new FileReader();

    audioElement.style.visibility = "visible";

    reader.onload = (e) =>  {

        let base64URL = e.target.result;

        if (!audioElementSource)
            createSourceForAudioElement();

        audioElementSource.src = base64URL;

        let BlobType = recordedBlob.type.includes(";") ?
            recordedBlob.type.substr(0, recordedBlob.type.indexOf(';')) : recordedBlob.type;
        
        audioElementSource.type = BlobType;

        audioElement.load();

        console.log("Playing Audio!");

    };

    reader.readAsDataURL(recordedBlob);

}