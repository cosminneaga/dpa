function save() {
    editor.save().then((output) => {
        console.log('Data: ', output);
    }).catch((error) => {
        console.log('Saving failed: ', error)
    });
}



async function getMe() {

    const res = await fetch(url + 'api/blogger/user/me', {
        headers: {
            'X-Access-Token': getCookie('X-Access-Token')
        }
    })
    const data = await res.json()
    localStorage.setItem('userId', data.data._id)
    const ul = document.querySelectorAll('.user-list')
    for (const list of ul) {
        const li = document.createElement('li')
        li.innerHTML = `${data.data['first_name']} ${data.data['last_name']} | ${data.data['email']}`
        list.appendChild(li)
    }

}

async function getBlogs() {

    const userId = JSON.parse(localStorage.getItem('blogger'))['user']['_id']

    const res = await fetch(url + 'api/blogger/blogs/' + userId)
    const data = await res.json()
    const tbody = document.querySelector('.blogs')
    for (const blog of data.data) {
        console.log("🚀 ~ file: panel.html ~ line 94 ~ getBlogs ~ blog", blog)
        let linksList = ''
        for (const authorLink of blog.author.links) {
            linksList += `<li>${authorLink}</li>`
        }
        console.log("🚀 ~ file: panel.html ~ line 139 ~ getBlogs ~ linksList", linksList)

        const tr = document.createElement('tr')

        tr.innerHTML = `
        <td>${blog._id}</td>
        <td>${blog.title}</td>
        <td>${blog.description}</td>
        <td>${blog.date}</td>
        <td>
            <ul>
                <li>${blog.author.name}</li>
                <li>${blog.author.links}</li>
            </ul>
        </td>
        `



        tbody.appendChild(tr)
    }

}



// DRAWER
function toggleDrawer() {
    const drawer = document.querySelector('.drawer')
    drawer.classList.toggle('active')
}

function closeDrawer() {
    const drawer = document.querySelector('.drawer')
    if (drawer.classList.contains('active')) drawer.classList.remove('active')
}


document.addEventListener('click', function (event) {
    const drawerBtn = document.querySelector('.drawer-button')
    const drawer = document.querySelector('.drawer')
    if (drawerBtn.contains(event.target)) {
        return
    } else if (!drawer.contains(event.target)) {
        closeDrawer()
    }
})

const drawer = document.querySelector('.drawer')
for (const child of drawer.children) {
    if (child.tagName === 'UL') {
        for (const c of child.children) {
            c.addEventListener('click', function () {
                closeDrawer()
            })
        }
    }
}

// getMe()
getBlogs()




const editor = new EditorJS({
    holder: 'editorjs',
    /**
         * Available Tools list.
         * Pass Tool's class or Settings object for each Tool you want to use
         */
    tools: {
        header: Header,
        delimiter: Delimiter,
        paragraph: {
            class: Paragraph,
            inlineToolbar: true,
        },
        embed: Embed,
        image: SimpleImage,
        linkTool: {
            class: LinkTool,
            config: {
                endpoint: 'http://localhost:8008/fetchUrl', // Your backend endpoint for url data fetching,
            }
        }
    }
}
);