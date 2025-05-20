import { csrfFetch } from "./csrf";

const DICTIONARY_SEARCH = "DICTIONARY_SEARCH"

const search = (meaning) => ({
    type: DICTIONARY_SEARCH,
    meaning
})

export const searchMeaning = (word) => async (dispatch) => {
    const response = await csrfFetch(`/api/dictionary/?word=${encodeURIComponent(word)}`, {
        method: 'GET'
    });
    if(response.ok) {
        const meaning = await response.json();
        dispatch(search(meaning));
        return meaning
    }
};

export default searchMeaning