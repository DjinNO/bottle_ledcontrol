<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
Команды:<br>
<a href="/random">Random</a></p><br>
<a href="/off">Off</a></p><br>
Пример команд:<br>
<br>
    <form method="post" action="send">
        <div>
            <label for="color">Color:</label>
            <input type="text" id="color" name="color">
        </div>
        <div>
            <label for="start">Start:</label>
            <input type="text" id="start" name="start">
        </div>
        <div>
            <label for="len">Len:</label>
            <input type="text" id="len" name="len">
        </div>
        <div>
            <label for="brightness">Brightness(0-255):</label>
            <input type="text" id="brightness" name="brightness">
        </div>
        <button type="submit">Send</button>
    </form>
<br>
<b>/fill?color=FF0000&start=0&len=5&brightness=255</b>  (Заполнит первые 5 светодиодов красным цветом с максимальной яркостью.)
</body>
</html>
