<script>
  import { recommend } from "../client";
  import "../app.postcss";
  import {
    brands,
    displays,
    gpu_brands,
    gpu_types,
    cores,
    storage_caps,
    storage_type,
    processor_brand,
    processors,
    rams,
  } from "../tags";
  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();

  export let activeTag = "none";

  // Params for recommendation engine
  let searchParams = [];
  let results;

  // Get appropriate data using keys
  let data = {
    brand: brands,
    display: displays,
    "gpu-brand": gpu_brands,
    "gpu-type": gpu_types,
    cores: cores,
    "storage-cap": storage_caps,
    "storage-type": storage_type,
    "processor-brand": processor_brand,
    processor: processors,
    ram: rams,
    none: [],
  };

  async function Recommend() {
    if (searchParams.length === 0)
        alert("No Params Selected!");
    else {
        results = await recommend(searchParams);
        dispatch("results", { value: results });
    }
  };

  const handleParamChange = (tag) => {
    searchParams.some((val) => {
      if (val === tag) return true;
      else return false;
    })
      ? (searchParams = searchParams.filter((val) => {
          if (val === tag) return false;
          else return true;
        }))
      : searchParams.push(tag);
    dispatch("paramChange", { value: searchParams });
  };
</script>

<div class="flex flex-col">
  <button
    class="btn btn-accent w-48 h-12 mb-4 rounded-none border-none"
    on:click={Recommend}
  >
    RECOMMEND
  </button>

  <div class="w-48 h-80 mr-4 border border-neutral overflow-y-scroll">
    <div class="flex gap-4 flex-wrap justify-center my-2">
      {#each data[activeTag] as tag}
        <button
          class="btn w-[80%]"
          on:click={() => {
            handleParamChange(tag);
          }}>{tag}</button
        >
      {/each}
    </div>
  </div>
</div>
