<script>
	import '../app.postcss';

	import SearchBar from '../components/SearchBar.svelte';
	import ResultBox from '../components/ResultBox.svelte';
    import ThemeController from '../components/ThemeController.svelte';
	import DisplayTags from '../components/DisplayTags.svelte';
	import Params from '../components/Params.svelte';

	let activeTag;
	let recommendedResults;
	let searchParams;

	function getSubTags(event) {
		activeTag = event.detail.category;
	}

	function displayResults(event) {
		recommendedResults = event.detail.value;
	}

	function updateParams(event) {
		searchParams = event.detail.value;
	}

	//TODO: add event for CTRL + K
	// TODO: show params

</script>

<div class="flex flex-col justify-center h-screen items-center">
	
    <div class="flex w-[60rem] justify-between">

		<h1 class="text-accent my-8">L A P R E C</h1>

		<!-- Toggle themes -->
        <ThemeController />
		
	</div>

	<div class="flex">

		<!-- Select tags from a category -->
		<DisplayTags {activeTag} on:results={displayResults} on:paramChange={updateParams}/>

		<!-- See Results -->
		<ResultBox results={recommendedResults}/>

	</div>

	<!-- Active Params -->

	<Params {searchParams} />

	<!-- The Search Bar -->
	<SearchBar on:displaySubTags={getSubTags}/>

	<div class="flex justify-evenly my-12 w-96">
		<p>🔷 Sadeem</p>
		<p>🟣 Abdullah</p>
		<p>🟨 Hassan</p>
	</div>
</div>
