<script>
    import { recommend } from '../client';
    import '../app.postcss';
    import { brands, displays, gpu_brands, gpu_types, cores, storage_caps, storage_type, processor_brand, processors, rams } from '../tags';

    export let activeTag = 'none';

    // Params for recommendation engine
    let searchParams = []

    // Get appropriate data using keys
    let data = {
        "brand": brands,
        "display": displays,
        "gpu-brand": gpu_brands,
        "gpu-type": gpu_types,
        "cores": cores,
        'storage-cap': storage_caps,
        'storage-type': storage_type,
        'processor-brand': processor_brand,
        'processor': processors,
        'ram': rams,
        'none': []
    };

    // TODO: Add recommendation function linked with button
    // TODO: Pass params as dispatch to show on main page

</script>

<div class="flex flex-col">
    <button class="btn btn-accent w-48 h-12 mb-4 rounded-none border-none">RECOMMEND</button>
    
    <div class="w-48 h-80 mr-4 border border-neutral overflow-y-scroll">
        <div class="flex gap-4 flex-wrap justify-center my-2">
            {#each data[activeTag] as tag}
                <button class="btn w-[80%]"
                on:click={() => {
                    // TODO: maybe make this a function to use later in deleting params through ui
                    searchParams.some((val) => {
                        if (val === tag) return true
                        else return false;
                    }) ? searchParams = searchParams.filter((val) => {
                        if (val === tag) return false
                        else return true
                    }) : searchParams.push(tag);
                }}>{tag}</button>
            {/each}
        </div>
    </div>
</div>
