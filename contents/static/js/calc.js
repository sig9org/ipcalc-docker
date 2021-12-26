$(function () {
  var $input_text = $('#input_text');

  function send() {
    var textData = JSON.stringify({ "text": $("#input_text").val() });
    $.ajax({
      type: 'POST',
      url: '/',
      data: textData,
      contentType: 'application/json',
      success: function (data) {
        var result = JSON.parse(data.ResultSet).result;
        $("#resulttext").html(result)
      }
    });
  };

  var send_timeout_id = null
  $input_text.on('keyup', function () {
    if (send_timeout_id) {
      clearTimeout(send_timeout_id);
    }
    send_timeout_id = setTimeout(send, 500);
  });
});