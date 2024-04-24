import axios from "axios";

const url = 'http://localhost:5000/recommend';

async function sendTags(tags) {
    try {
        const response = await axios.post(url, {search_tags: tags});
        const data =  response.data;

        if (data.error) {
            throw new Error(data.error);
        }
        console.log("Results:", data.results);

    } catch (error) {
        console.error("Error:", error.messsage);
    }
}

export let recommend = (tags) => {
    sendTags(tags);
}