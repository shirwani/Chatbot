function sendContentToApp(){
    var xhr = new XMLHttpRequest();
    var user_message = document.getElementById("user_message").value
    var url = window.location.href + '/chat';

    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById('chat_log').innerHTML = xhr.responseText;
            document.getElementById('user_message').value = "";
        }
    };

    let json_data = {
        "user_message": user_message
    }

    xhr.send(JSON.stringify(json_data));

    clearTextarea();
}

function clearChat(){
    var xhr = new XMLHttpRequest();
    var url = window.location.href + '/clear';

    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById('chat_log').innerHTML = xhr.responseText;
        }
    };

    xhr.send({});
    clearTextarea();
}

function autoExpand(textarea) {
    textarea.style.height = "auto";  // Reset height to recalculate
    textarea.style.height = textarea.scrollHeight + "px"; // Set new height
}

function clearTextarea() {
    let textarea = document.getElementById("user_message");
    textarea.value = "";
    textarea.style.height = "40px"; // Reset to default height
}