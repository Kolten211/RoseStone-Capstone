import { csrfFetch } from "./csrf";

const initialState = []

const GET_WORDS = "GET_WORDS"
const WORD_DETAILS = "WORD_DETAILS"
const CLEAR_WORD_DETAILS = 'CLEAR_WORD_DETAILS'
const CREATE_WORD = "CREATE_WORD"
const DELETE_WORD = "DELETE_WORD"
const UPDATE_WORD = "UPDATE_WORD"
const GETLEARNEDWORDS= "GETLEARNEDWORDS"

const getWord = (words) => ({
    type: GET_WORDS,
    words
})

const createWord = (word) => ({
    type: CREATE_WORD,
    word
})

const wordDetails = (word) => ({
    type: WORD_DETAILS,
    word
})

export const clearWordDetails = () => ({
    type: CLEAR_WORD_DETAILS
});

const updateWord = (word_id, updatedWord) => ({
    type: UPDATE_WORD,
    word_id,
    updatedWord
})

const deleteWord = (word_id) => ({
    type: DELETE_WORD,
    word_id
})

const get_learned_words = (words) => ({
    type: GETLEARNEDWORDS,
    words
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

export const fetchLearnedWords = () => async (dispatch) => {
    const response = await csrfFetch('/api/words/learned')
    console.log('Response', response)

    if (response.ok) {
        const learnedWords = await response.json();
        console.log("what is happening", learnedWords)
        dispatch(get_learned_words(learnedWords))
        return learnedWords
    } else {
        throw new Error('Failed to find words')
    }
}

export const fetchLWDetails = (word_id) => async (dispatch) => {
    const response = await csrfFetch(`/api/words/learned/${word_id}`)
    if (response.ok) {
        const data = await response.json()
        dispatch(wordDetails(data))
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

export const editWord = ({id, wordData}) => async (dispatch) => {
    console.log("What do you have?", wordData)
    console.log("ID", id)
    const response = await csrfFetch(`/api/words/${id}`, {
        method: 'PUT',
        // headers: {
        //     'Content-Type': 'application/json'
        // },
        body: wordData
    });
    for (let [key, value] of wordData.entries()) {
        console.log("THUNK", key, value);
      }
    console.log("Response", response)
    if (response.ok) {
        const updatedWord = await response.json();
        console.log("is this the word", updatedWord)
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
        case GETLEARNEDWORDS:
            return[...state, action.words]
        case WORD_DETAILS:
            console.log(action)
            return [...state.filter(spot => spot.id !== action.spot.id), action.word]
        case CREATE_WORD:
            return [...state, action.word];
        case UPDATE_WORD:
            return state.map((word) => word.id === action.word_id ? action.word : word);
        case DELETE_WORD:
            return state.map((word => word.id !== action.word_id))
        case CLEAR_WORD_DETAILS:
            return initialState;
        default:
            return state
    }
}

export default wordReducer
