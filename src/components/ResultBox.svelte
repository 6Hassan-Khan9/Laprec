<script>
    export let results = [];
</script>

<div class="w-[60rem] h-96 mb-12 border border-neutral overflow-y-scroll">

    <table class="table table-zebra text-xl">
        <thead>
            <tr>
                <th></th>
                <th>Laptop</th>
            </tr>
        </thead>
        <tbody>
            {#each results as row, index}
                <tr>
                    <th>{index + 1}</th>
                    <td>{row}</td>
                </tr>
            {/each}
        </tbody>
    </table>
</div>