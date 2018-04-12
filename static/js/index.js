$(document).ready(function() {
  M.AutoInit();
  startApp();
});

var startApp = function() {
  gapi.load("auth2", function() {
    // Retrieve the singleton for the GoogleAuth library and set up the client.
    var auth2 = gapi.auth2.init({
      client_id: $("meta[name='google-signin-client_id']").attr("content"),
      cookie_policy: "single_host_origin",
      fetch_basic_profile: true
    });
    $("#gPlusSignIn").click(function() {
      auth2
        .grantOfflineAccess({
          redirect_uri: "postmessage",
          approval_prompt: "force"
        })
        .then(signInCallback);
    });
  });
};

var signInCallback = function(authResult) {
  if (authResult["code"]) {
    // Unhide the loader
    $("#loader ").removeClass("hide");
    // Send the one-time-use code to the server, if the server responds, write a 'login successful' message to the web page and then redirect back to the main restaurants page
    $.ajax({
      type: "POST",
      url: "/gconnect?state=" + window.token,
      processData: false,
      data: authResult["code"],
      contentType: "application/octet-stream; charset=utf-8",
      success: function(result) {
        // Handle or verify the server response if necessary.
        if (result) {
          if (result.next) window.location = result.next;
          else location.reload();
        } else if (authResult["error"]) {
          console.error("There was an error: " + authResult["error"]);
        } else {
          console.error(
            "Failed to make a server-side call. Check your configuration and console."
          );
        }
      }
    });
  }
};
