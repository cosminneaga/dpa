<template>
    <NuxtLayout>
        <section
            id="hero"
            class="my-5 elevation-3"
        >
            <div>
                <h1 class="text-h1 text-indigo-accent-4 font-weight-bold">Welcome to Blogger</h1>
            </div>
        </section>

        <section id="2">
            <p class="text-body-1">
                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Laudantium eius tenetur quae in cupiditate atque
                inventore. Culpa iste ea quasi est harum officiis consectetur ipsum quis nam, architecto sequi consequuntur rem
                quidem aspernatur facere atque quae blanditiis soluta, dolor, qui molestiae. Ab vel quae soluta nisi a
                reprehenderit ducimus rem vitae quia aliquid eligendi eaque, pariatur, quos fuga voluptatum omnis rerum nihil
                nam quidem totam veritatis voluptas molestiae sed cum. Esse commodi laudantium iusto ex eaque fugiat? Tempora,
            </p>
        </section>

    </NuxtLayout>
</template>

<script>
export default {
    async mounted() {
        const res = await $fetch("http://localhost:8080/hello");
        console.log(res);
    },
};
</script>

<style lang="scss" scoped>
section#hero {
    display: flex;
    justify-content: center;
    background-image: url("/img/hero.jpg");
    background-position: center;
    background-size: cover;
    height: 400px;
    & div {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 75%;
        text-align: center;
    }
}
</style>