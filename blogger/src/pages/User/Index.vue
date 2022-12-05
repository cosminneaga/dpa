<template>
    <section></section>
</template>

<script lang="ts">
export default {
    async mounted() {
        const req = await this.axios.get('/api/user/me', {
            headers: {
                'x-access-token': this.$cookies.get('X-Access-Token')
            }
        })

        console.log(req.data.data);
        
    }
}
</script>