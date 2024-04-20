<script>
	import '../app.postcss';

	import Search from '../components/Search.svelte';
	import DisplayBox from '../components/ResultBox.svelte';
    import ThemeController from '../components/ThemeController.svelte';
	import DisplayTags from '../components/DisplayTags.svelte';

</script>

<div class="flex flex-col justify-center h-screen items-center">
	
    <div class="flex w-[60rem] justify-between">

		<h1 class="text-accent my-12">L A P R E C</h1>

        <ThemeController />
		
	</div>

	<div class="flex">
		<DisplayTags />
		<DisplayBox />
	</div>

	<Search />

	<div class="flex justify-evenly my-12 w-96">
		<p>Sadeem</p>
		<p>Abdullah</p>
		<p>Hassan</p>
	</div>
</div>
