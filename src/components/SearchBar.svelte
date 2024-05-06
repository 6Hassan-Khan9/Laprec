<script>
  import { createEventDispatcher } from "svelte";
  
  const dispatch = createEventDispatcher();

  let categories = [
    "brand",
    "display",
    "gpu-brand",
    "gpu-type",
    "cores",
    "storage-cap",
    "storage-type",
    "processor-brand",
    "processor",
    "ram",
  ];

  let selected_category;

  let filtered_categories = [];
  let search_value;
  let rendered_categories;

  const filterCategories = () => {
    if (search_value === "") filtered_categories = [];
    else if (search_value === 'all') filtered_categories = [...categories];
    else
      filtered_categories = [
        ...categories.filter((elem) => elem.includes(search_value)),
      ];
  };

  $: rendered_categories = filtered_categories;
</script>

<!-- Search bar -->
<div class="flex">
    <button class="btn rounded-none btn-accent" on:click={() => {
        dispatch('displaySubTags', {
            category: selected_category
        })
    }}>S</button>
    <label
      class="input flex items-center gap-2 w-[57.5rem] border border-accent rounded-none"
    >
      <input
        type="text"
        class="grow"
        placeholder="Search"
        on:keyup={filterCategories}
        bind:value={search_value}
      />
      <kbd class="kbd kbd-m text-accent">CTRL</kbd>
      <p>+</p>
      <kbd class="kbd kbd-m text-accent">K</kbd>
    </label>
</div>

<div class="w-[60rem] h-96 border border-neutral rounded-none">
  <div class="flex flex-wrap my-4 gap-4 justify-center">
    {#each rendered_categories as category}
      <button
        class="btn flex-grow-0 w-52"
        class:btn-accent={selected_category === category}
        on:click={() => {
          if (selected_category === category) {
            selected_category = '';
          } else selected_category = category;
        }}>{category}</button
      >
    {/each}
  </div>
</div>
