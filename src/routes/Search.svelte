<script>
	import '../app.postcss';

	import Search from '../components/Search.svelte';
	import DisplayBox from '../components/DisplayBox.svelte';
    import ThemeController from '../components/ThemeController.svelte';

</script>

<div class="flex flex-col justify-center h-screen items-center">
	
    <div class="flex w-[60rem] justify-between">

		<h1 class="text-accent my-12">L A P R E C</h1>

        <ThemeController />
		
	</div>

	<div class="flex">
		<div class="w-48 h-96 mr-4 border border-neutral"></div>
		<DisplayBox />
	</div>
	<Search />

	<div class="flex justify-evenly my-12 w-96">
		<p>Sadeem</p>
		<p>Abdullah</p>
		<p>Hassan</p>
	</div>
</div>
