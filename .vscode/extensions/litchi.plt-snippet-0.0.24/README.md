# Plt Snippet

**目前还是预览版，各种接口可能随时会变化，如果最新版有使用问题请在插件页面将插件回退到之前的版本！**

plt-snippet是一个提供matplotlib代码片段的软件，
旨在平缓matplotlib的学习曲线并降低其使用门槛。

+ matplotlib的新用户可以使用GUI来帮助记忆绘图 API
+ matplotlib的老用户可以快速插入代码片段
+ 机构可以定制自己的绘图流程

## Features

仅提供代码片段，可以简单修改后画图。

## Requirements

matplotlib是一个用于数据可视化的Python包，使用前确保已安装：
```sh
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib
```

推荐在`ipynb`文件中使用此插件，
在 VS Code 中新建后缀为`.ipynb`的文件后将自动推荐相关插件，
视网络情况可能需要手动安装`ipykernel`
```sh
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ipykernel
```

同时保证 `VS Code` 版本高于 `1.72.0`。


## Extension Settings

* `plt-snippet.fontPath`: 配置本地字体路径，例如`C:\\Users\\username\\Documents\\fonts\\songTimes.ttf`


如果有问题可以发邮件到`litchi.code@foxmail.com`或者在插件评论区中评论。

### 自定义模板

本插件提供自定义绘图任务模板功能，用户可以将自己常用的绘图脚本制作成`notebook`文件（后缀名为`ipynb`），
然后通过下述流程便可以通过`自定义模板`按钮调出模板浏览界面并使用相应模板来创建新任务。
事实上这也不局限于`Matplotlib`任务脚本，用户也可以添加其它自己常用的脚本，例如数据滤波、拟合等。

1. 首先用户需要准备好自己的`ipynb`文件和相应的封面图片，其中封面图片建议长宽比近似为 1:1，同时图片尺寸建议控制在 100kB 以下；
然后编写一个如下的`html`文件，可以复制下面内容，然后只需要修改`<div class="container">`中的内容，主要参数含义如下：
+ `h2`中的汉字: 本组若干个脚本的标题，建议将功能相近的脚本添加到同一组中
+ `img`元素中的`src`内容：指向封面图片的相对路径，相对html文件的路径
+ `id`值：建议给一个独一无二的编号，可以为`组名`+`数字或含义`
+ `data-ipynbpath`的值：绘图脚本的绝对路径
+ `button`元素的字符：按钮上将体现的文字，建议为脚本的功能描述，字数尽量简短些，不要超过12个汉字

编写`html`和`notebook`任务文件的其它注意：
+ 如果你了解`css样式表`，那么你可以修改`<style>`标签内的内容为自己喜欢的样式，但是并不推荐
+ 不要修改底部`<script>`标签内的内容
+ 建议将同组任务放在同一个文件夹中


2. 编写完成后，在 VS Code 中按`F1`键调出命令面板，然后输入`define custom template`后会显示相应命令，点击后会调出文件选择对话框，选择上面编写的`html`文件便会进入模板`HTML`制作，根据模板的数量不同等待时间也不同，通常会瞬间完成。制作过程中不会检测`notebook`文件是否存在，但会读取封面文件，如果读取失败那么会使用默认的封面进行替代。

3. 模板制作完成后，在 VS Code 中使用快捷键`Ctrl + ,`调出设置界面，在左侧目录选择选择扩展然后定位到`Plt Snippet`，在`Custom Template HTML`一项中填写上面制作的模板`HTML`路径，注意你需要使用双斜线来进行路径分割符的转义，例如：
```txt
D:\\path\\to\\customTemplate.html
```


```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>自定义模板</title>
    <style>
        h2 {
            text-align: center;
            /* 文本居中 */
            width: 100vw;
            /* 设置宽度为视口宽度的100%，使得h2元素全宽 */
            margin: 0;
            /* 清除默认的外边距，可根据需要调整上下的外边距 */
            background-color: var(--vscode-button-background);
            color: var(--vscode-button-foreground);
        }

        img {
            border: 2px solid var(--vscode-button-background);
            /* 设置边框宽度、样式和颜色 */
        }

        .container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }

        .box {
            width: 240px;
            height: 240px;
            margin: 10px;
            text-align: center;
        }

        button {
            border: none;
            margin-top: 2px;
            padding: var(--input-padding-vertical) var(--input-padding-horizontal);
            width: 80%;
            text-align: center;
            outline: 1px solid transparent;
            outline-offset: 2px !important;
            color: var(--vscode-button-foreground);
            background: var(--vscode-button-background);
            font-size: 16px;
        }

        button:hover {
            cursor: pointer;
            background: var(--vscode-button-hoverBackground);
        }

        button:focus {

            outline-color: var(--vscode-focusBorder);
        }

        button.secondary {
            color: var(--vscode-button-secondaryForeground);
            background: var(--vscode-button-secondaryBackground);
        }

        button.secondary:hover {
            background: var(--vscode-button-secondaryHoverBackground);
        }

        .box img {
            width: 100%;
            height: 80%;
        }
    </style>
</head>
<body>
    <!-- 修改这里的内容 -->
    <div class="container">  
        <h2>第一组名称</h2>
        <div class="box">
            <img src="https://github.com/nfvm/plt-snippet/raw/HEAD/relative_path_to/a.png" alt="item-a">
            <button id="a" data-ipynbpath="D:absolute_path_to\a.ipynb">item-a</button>
        </div>
        <div class="box">
            <img src="https://github.com/nfvm/plt-snippet/raw/HEAD/relative_path_to/b.png" alt="item-b">
            <button id="b" data-ipynbpath="D:absolute_path_to\b.ipynb">item-b</button>
        </div>
        <h2>第二组名称</h2>
        <div class="box">
            <img src="https://github.com/nfvm/plt-snippet/raw/HEAD/relative_path_to/c.png" alt="item-c">
            <button id="c" data-ipynbpath="D:absolute_path_to\c.ipynb">item-c</button>
        </div>
        <div class="box">
            <img src="https://github.com/nfvm/plt-snippet/raw/HEAD/relative_path_to/d.png" alt="item-d">
            <button id="d" data-ipynbpath="D:absolute_path_to\d.ipynb">item-d</button>
        </div>
    </div>
    <!-- 修改内容截至到这里 -->
    <script>
        const vscode = acquireVsCodeApi();

        const buttons = document.querySelectorAll('button');

        buttons.forEach(button => {
            button.addEventListener('click', function () {
                vscode.postMessage({
                    "id": this.id,
                    "ipynbpath": this.dataset.ipynbpath
                });
            });
        });
    </script>
</body>

</html>
```



## TODO

+ 完善模板功能
+ 细致化侧边栏的按钮

