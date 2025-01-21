import { csrfFetch } from "./csrf";

const initialState = []

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
        throw new Error('Failed to find words')
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
        throw new Error('Failed to add word')
    }
};

export const editWord = (wordData) => async (dispatch) => {
    const response = csrfFetch(`/api/words/${wordData.id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: response.stringify(wordData)
    });

    if (response.ok) {
        const updatedWord = await response.json();
        dispatch(updateWord(updatedWord));
        return updatedWord
    } else {
        throw new Error('Failed to update word');
    }
};

export const removeWord = (word_id) => async (dispatch) => {
    const response = await csrfFetch(`/api/words/${word_id}`, {
        method: 'DELETE'
    })

    if (response.ok) {
        dispatch(deleteWord(word_id))
    } else {
        throw new Error('Failed to delete word');
    }
};

const wordReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_WORDS:
            return [...action.words];
        case CREATE_WORD:
            return [...state, action.word];
        case UPDATE_WORD:
            return state.map((word) => word.id === action.word_id ? action.word : word);
        case DELETE_WORD:
            return state.map((word => word.id !== action.word_id))
        default:
            return state
    }
}

export default wordReducer
