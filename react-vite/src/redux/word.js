import { csrfFetch } from "./csrf";

const GET_WORDS = "GET_WORDS"
const CREATE_WORD = "CREATE_WORD"
const DELETE_WORD = "DELETE_WORD"
const UPDATE_WORD = "UPDATE_WORD"


const getWord = (words) => ({
    type: GET_WORDS,
    words
})

const createWord = (word) => ({
    type: CREATE_WORD,
    word
})

const updateWord = (word_id, updatedWord) => ({
    type: UPDATE_WORD,
    word_id,
    updatedWord
})

const deleteWord = (word_id) => ({
    type: DELETE_WORD,
    word_id
})



export const fetchWords = () => async (dispatch) => {
    const response = await csrfFetch('/api/words/');

    if (response.ok) {
        const words = await response.json();
        dispatch(getWord(words))
    } else {
        return {'message': 'Error somthing isn\'t right' }
    }
}

export const addWord = (wordData) => async (dispatch) => {
    const response = csrfFetch('/api/words/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(wordData)
    });
    if (response.ok) {
        const newWord = await response.json();

        dispatch(createWord(newWord))
    } else {
        return {'message': 'Error somthing isn\'t right'}, 400
    }
}


