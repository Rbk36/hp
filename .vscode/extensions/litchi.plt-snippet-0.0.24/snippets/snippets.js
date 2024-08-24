const vscode = acquireVsCodeApi();
let clickCount = 0;
let timer;

const buttons = document.querySelectorAll('button');

// 假设buttons是一个包含你想要添加事件监听器的按钮元素的数组
buttons.forEach(button => {
    button.addEventListener('click', function(event) {
        clickCount++;

        if (timer) {
            clearTimeout(timer);
        }

        timer = setTimeout(() => {
            if (clickCount === 1) {
                vscode.postMessage({
                    "id": this.id,
                    "snippets": this.dataset.snippets,
                    "comment": this.dataset.comment,
                    "event": "click"
                });
            }
            else {
                vscode.postMessage({
                    "id": this.id,
                    "snippets": this.dataset.snippets,
                    "comment": this.dataset.comment,
                    "event": "doubleClick"
                });
            }
            clickCount = 0;
        }, 300);
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const colorPicker = document.getElementById('color');
    const colorValueDisplay = document.getElementById('colorValue');

    // 监听颜色选择器的 input 事件
    colorPicker.addEventListener('input', function (event) {
        const newColor = event.target.value;
        colorValueDisplay.textContent = newColor;

    });

    colorPicker.addEventListener('blur',  function(){
        copyColorValue();
    });
});

// 复制颜色值的函数
function copyColorValue() {
    const colorValueDisplay = document.getElementById('colorValue');
    const colorValue = colorValueDisplay.textContent.trim();
    navigator.clipboard.writeText(colorValue);
}
