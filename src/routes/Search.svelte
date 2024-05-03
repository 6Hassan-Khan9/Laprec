<script>
	import '../app.postcss';

	import SearchBar from '../components/SearchBar.svelte';
	import ResultBox from '../components/ResultBox.svelte';
    import ThemeController from '../components/ThemeController.svelte';
	import DisplayTags from '../components/DisplayTags.svelte';

	let activeTag;

	function getSubTags(event) {
		activeTag = event.detail.category;
	}

	//TODO: add event for CTRL + K

</script>

<div class="flex flex-col justify-center h-screen items-center">
	
    <div class="flex w-[60rem] justify-between">

		<h1 class="text-accent my-8">L A P R E C</h1>

		<!-- Toggle themes -->
        <ThemeController />
		
	</div>

	<div class="flex">

		<!-- Select tags from a category -->
		<DisplayTags {activeTag}/>

		<!-- See Results -->
		<ResultBox />

	</div>

	<!-- The Search Bar -->
	<SearchBar on:displaySubTags={getSubTags}/>

	<div class="flex justify-evenly my-12 w-96">
		<p>🔷 Sadeem</p>
		<p>🟣 Abdullah</p>
		<p>🟨 Hassan</p>
	</div>
</div>
