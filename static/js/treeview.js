$(document).ready(function(){
    $("#browser").treeview({
        toggle: function() {
            console.log("%s was toggled.", $(this).find(">span").text());
        }
    });
});