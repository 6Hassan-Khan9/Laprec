<script>
  import { Router, Route } from 'svelte-routing';
  import Index from './routes/Index.svelte';
  import Search from './routes/Search.svelte';
</script>

<Router>

  <Route component={Index}/>
  <Route path="/search" component={Search}/>

</Router>