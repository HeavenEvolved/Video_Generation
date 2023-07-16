//audio recording API

var audioRecorder = {

    audioBlobs: [],
    mediaRecorder: null,
    streamBeingCaptured: null,

    start: function ()  {

        if (!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia))   {
            console.log("No mediaDevices API or getUserMedia method available.");
        }

        else{
            return navigator.mediaDevices.getUserMedia({ audio: true })
                .then(stream => {
                    
                    audioRecorder.streamBeingCaptured = stream;
                    audioRecorder.mediaRecorder = new MediaRecorder(stream);
                    audioRecorder.audioBlobs = [];

                    audioRecorder.mediaRecorder.addEventListener("dataavailable", event => {
                        audioRecorder.audioBlobs.push(event.data);
                    });

                    audioRecorder.mediaRecorder.start();

                })
        }

    },

    stop: function ()   {
        
        return new Promise(resolve =>   {

            let mimeType = 'audio/wav; codecs=opus';

            audioRecorder.mediaRecorder.addEventListener("stop", () =>  {
                let audioBlob = new Blob(audioRecorder.audioBlobs, { type: mimeType});

                resolve(audioBlob);
            })

            audioRecorder.cancel();
        
        })
    },

    cancel: function()  {

        audioRecorder.mediaRecorder.stop();

    }

}