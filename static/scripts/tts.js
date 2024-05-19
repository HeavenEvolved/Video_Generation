var sentenceElement = document.getElementsByName("sentence")[0];
var speakerElement = document.getElementsByName("speaker")[0];
var languageElement = document.getElementsByName("language")[0];

var submitButton = document.getElementsByClassName("submit")[0];

submitButton.onclick = submitData;

function mainMenu()    {

    var xmlhttp = new XMLHttpRequest();

    var fd = new FormData();

    fd.set('choice', 'main');

    xmlhttp.onload = function() {

        console.log(this.response);

    }

    var url = '/tts';

    xmlhttp.open("POST", url, true);
    xmlhttp.send(fd);

}

function previousMenu() {

    location.reload();

}

var file;

var hasFile = false;

function validateAndUpload(input)   {

    file = input.files[0];

    if(file)
        hasFile = true;

    console.log(file['type'].substring(("video/").length,));

}

function submitData()   {

    console.log("Submitting Data");

    var xmlhttp = new XMLHttpRequest();

    var fd = new FormData();

    fd.set('sentence', sentenceElement.value);
    fd.set('speaker', speakerElement.value);
    fd.set('language', languageElement.value);

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

    var url = '/tts';

    xmlhttp.open("POST", url, true);
    xmlhttp.send(fd);


}