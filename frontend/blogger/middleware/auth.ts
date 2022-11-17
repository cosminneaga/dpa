export default defineNuxtRouteMiddleware(async (to, from) => {
    // isAuthenticated() is an example method verifying if an user is authenticated
    if (await isAuthenticated() === false) {
        return navigateTo('/login')
    }
})


async function isAuthenticated() {
    const bloggerLS = localStorage.getItem('blogger')

    if (bloggerLS) {
        const bbb = JSON.parse(bloggerLS)
        if (bbb?.token) {

            const res = await $fetch('http://localhost:8080/api/blogger/user/me', {
                headers: {
                    'X-Access-Token': bbb.token
                }
            })
            console.log('middleware/auth/isAuthenticated()');

            console.log(res);

            return true
        }
        return false
    }
    return false

}

