function show_response(response, statusText, xhr, $form)  { 
  if(!response.success) {
    $(response.data).each(function(i, element) {
      $("#"+element[0]+"_wrapper").addClass("ui-state-error");
      $("#"+element[0]+"_wrapper .error").append(element[1]);
    });        
    
    $.notification.error(response.message);
  } else {
    $.notification.notice(response.message);
    $("h1").text("test run directory: " + $('#id_name').val());

    $('#application-tree').jstree('refresh', "#"+response.data.parent_id+"_testrundirectory", response.data);

    $('#application-tree').bind("refresh.jstree", function (event, data) {
      $("#application-tree").jstree("open_node", "#"+data.args[1].parent_id+"_testrundirectory", function() {
        $("#application-tree").jstree("select_node", "#"+data.args[1].current_id+"_testrundirectory", true);
        document.location.hash = '#testrundirectory/'+ data.args[1].current_id +"/edit/";
      });
    });
  }
}

function clear_errors(arr, $form, options) { 
  $('.field-wrapper').removeClass('ui-state-error');
  $('.field-wrapper .error').text("");
}

$(function() {
  $('#testrundirectory_form').ajaxForm({ 
    success: show_response,
    beforeSubmit: clear_errors
  });
});
