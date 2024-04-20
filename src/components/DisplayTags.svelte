<script>
    import { recommend } from '../client';
    import '../app.postcss';
    import { brands, displays, gpu_brands, gpu_types, cores, storage_caps, storage_type, processor_brand, processors, rams } from '../tags';

    export let activeTag = 'none';

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

</script>

<div class="w-48 h-96 mr-4 border border-neutral overflow-y-scroll">
    <div class="flex gap-4 flex-wrap justify-center my-2">
        {#each data[activeTag] as tag}
            <button class="btn w-[80%]">{tag}</button>
        {/each}
    </div>
</div>