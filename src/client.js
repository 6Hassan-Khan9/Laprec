import axios from "axios";

const url = 'http://localhost:5000/recommend';

async function sendTags(tags) {
    try {
        const response = await axios.post(url, {search_tags: tags});
        const data =  response.data;

        if (data.error) {
            throw new Error(data.error);
        }
        return data.results;

    } catch (error) {
        console.error("Error:", error.messsage);
    }
}

export async function recommend(tags) {
    let val = await sendTags(tags);
    return val;
}