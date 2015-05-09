JSONEditor.plugins.select2.width = "300px";
JSONEditor.defaults.options.theme = 'bootstrap3';

var editor = new JSONEditor(document.getElementById('editor_holder'), {
    ajax: true,

    schema: {
        type: "array",
        title: "Tweet Texts",
        items: {
            title: "Tweet",
            headerTemplate:"{{i}} - {{self.name}}",
            $ref: "influential.json"
        }
    }
});

document.getElementById('submit').addEventListener('click',function() {
    console.log(editor.getValue());
});

