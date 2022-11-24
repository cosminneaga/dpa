export default defineNuxtRouteMiddleware(async (to, from) => {
    // isAuthenticated() is an example method verifying if an user is authenticated
    if (await isAuthenticated() === false) {
        return navigateTo('/login')
    }
})




async function isAuthenticated() {

    if (process.client) {
        const bloggerLS = window.localStorage.getItem('blogger')

        if (bloggerLS) {
            const bbb = JSON.parse(bloggerLS)
            if (bbb?.token) {

                const res = await $fetch('http://localhost:8080/api/blogger/user/me', {
                    headers: {
                        'X-Access-Token': bbb.token
                    }
                })

                if (res.data.token === bloggerLS.token) {
                    return true
                }
                return false
            }
            return false
        }
        return false
    }

}