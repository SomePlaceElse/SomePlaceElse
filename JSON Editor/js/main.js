JSONEditor.plugins.select2.width = "300px";
JSONEditor.defaults.options.theme = 'bootstrap3';

var editor = new JSONEditor(document.getElementById('editor_holder'), {
    schema: {
        type: "object",
        title: "Tweet Text",
        properties: {
            Id: {
                type: "integer",
            },
            Text: {
                type: "string",
            },
            Class: {
                type: "string",
                enum: [
                    "Positive",
                    "Negative"
                ]
            }
        }
    }
});

document.getElementById('submit').addEventListener('click',function() {
    console.log(editor.getValue());
});

