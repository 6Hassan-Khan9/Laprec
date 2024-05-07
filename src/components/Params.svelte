<script>
    export let searchParams = [];
</script>

<div class="flex justify-start w-[60rem] h-28 mb-8">
    {#each searchParams as param}
        <div class="flex justify-center items-center bg-neutral h-full text-xl rounded-lg text-accent mx-4">
            <p class="px-8">{param}</p>
        </div>
    {/each}
</div>