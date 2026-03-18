<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Тест Telegram</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
</head>
<body style="text-align: center; padding: 50px; font-family: Arial;">
    <h1>🔍 ТЕСТОВАЯ СТРАНИЦА</h1>
    <p>Если вы это видите - HTML грузится</p>
    <p id="status" style="color: blue;">Проверка Telegram...</p>
    
    <button onclick="testTelegram()">Проверить Telegram API</button>
    
    <script>
        function testTelegram() {
            try {
                if (window.Telegram && Telegram.WebApp) {
                    document.getElementById('status').innerHTML = '✅ Telegram API работает!';
                    document.getElementById('status').style.color = 'green';
                    Telegram.WebApp.expand();
                } else {
                    document.getElementById('status').innerHTML = '❌ Telegram API НЕ работает';
                    document.getElementById('status').style.color = 'red';
                }
            } catch (e) {
                document.getElementById('status').innerHTML = '❌ Ошибка: ' + e.message;
            }
        }
        
        // Автоматическая проверка при загрузке
        setTimeout(testTelegram, 1000);
    </script>
</body>
</html>
