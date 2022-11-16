const url = 'http://localhost:8080/'
checkIfLoggedIn()

function toggleShowPassword(ids) {
    for (const id of ids) {
        const element = document.querySelector(id)
        if (element.type === 'password') {
            element.type = 'text'
        } else {
            element.type = 'password'
        }
    }
}

async function login(formId) {
    const formData = getFormData(formId)




    const res = await fetch(url + '/api/blogger/login', {
        method: 'post',
        headers: { 'Content-Type': 'application/json' },
        body: formData
    })
    const data = await res.json()
    if (res.status !== 200) {
        alert(data.message)
        return false
    } else {
        console.log(data);
        localStorage.setItem('blogger', JSON.stringify(data.data))
        checkIfLoggedIn()
    }
}

function checkIfLoggedIn() {
    const token = getCookie('X-Access-Token')
    if (token !== '') {
        const template = `
        <div style="text-align: center;">
            <h1>You are logged in!</h1>
            <a class='btn md' href='${url}blogger/panel'>Go to Panel</a>
        </div>`
        const loginContainer = document.querySelector('#login')
        const registerContainer = document.querySelector('#register')
        if (loginContainer && registerContainer) {
            loginContainer.innerHTML = template
            registerContainer.innerHTML = template
        }
    }
}


function getFormData(formId) {
    const formData = new FormData(document.getElementById(formId))
    const data = {}
    for (const pair of formData.entries()) {
        data[pair[0]] = pair[1]
    }
    return JSON.stringify(data)
}

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}