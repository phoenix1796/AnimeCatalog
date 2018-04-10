$(document).ready(function () {
    $(document).ready(function () {
        M.AutoInit();
    });
});

function signInCallback(authResult) {
    if (authResult['code']) {
        // Unhide the loader
        $("#loader ").removeClass("hide");
        // Send the one-time-use code to the server, if the server responds, write a 'login successful' message to the web page and then redirect back to the main restaurants page
        $.ajax({
            type: 'POST',
            url: '/gconnect?state=' + window.token,
            processData: false,
            data: authResult['code'],
            contentType: 'application/octet-stream; charset=utf-8',
            success: function (result) {
                // Handle or verify the server response if necessary.
                if (result) {
                    location.reload();
                } else if (authResult['error']) {
                    console.error('There was an error: ' + authResult['error']);
                } else {
                    console.error('Failed to make a server-side call. Check your configuration and console.');
                }
            }

        });
    }
}