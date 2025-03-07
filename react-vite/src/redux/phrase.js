import { csrfFetch } from "./csrf";

const initialState = []

const GET_PHRASES = "GET_PHRASES"
const GET_LEARNED_PHRASES = "GET_LEARNED_PHRASES"
const CREATE_PHRASE = "CREATE_PHRASE"
const DELETE_PHRASE = "DELETE_PHRASE"
const UPDATE_PHRASE = "UPDATE_PHRASE"


const getPhrase = (phrases) => ({
    type: GET_PHRASES,
    phrases
})

const getLearned = (phrases) => ({
    type: GET_LEARNED_PHRASES,
    phrases
})
const createPhrase = (phrase) => ({
    type: CREATE_PHRASE,
    phrase
})

const updatePhrase = (phrase_id, updatedphrase) => ({
    type: UPDATE_PHRASE,
    phrase_id,
    updatedphrase
})

const deletePhrase = (phrase_id) => ({
    type: DELETE_PHRASE,
    phrase_id
})



export const fetchPhrases = () => async (dispatch) => {
    const response = await csrfFetch('/api/phrases/');

    if (response.ok) {
        const phrases = await response.json();
        dispatch(getPhrase(phrases))
    } else {
        throw new Error('Failed to find phrases')
    }
}

export const fetchLearnedPhrases = () => async (dispatch) => {
    const response = await csrfFetch('api/phrases/learned');

    if (response.ok) {
        const phrases = await response.json();
        dispatch(getLearned(phrases))
    }
}
export const addPhrase = (phraseData) => async (dispatch) => {
    console.log("Phrase", phraseData)
    const response = await csrfFetch('/api/phrases/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(phraseData)
    });
    if (response.ok) {
        const newphrase = await response.json();

        dispatch(createPhrase(newphrase))
    } else {
        throw new Error('Failed to add phrase')
    }
};

export const editPhrase = (phraseData) => async (dispatch) => {
    const response = await csrfFetch(`/api/phrase/${phraseData.id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: response.stringify(phraseData)
    });

    if (response.ok) {
        const updatedphrase = await response.json();
        dispatch(updatePhrase(updatedphrase));
        return updatedphrase
    } else {
        throw new Error('Failed to update phrase');
    }
};

export const removePhrase = (phrase_id) => async (dispatch) => {
    const response = await csrfFetch(`/api/phrase/${phrase_id}`, {
        method: 'DELETE'
    })

    if (response.ok) {
        dispatch(deletePhrase(phrase_id))
    } else {
        throw new Error('Failed to delete phrase');
    }
};

const phraseReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_PHRASES:
            return [...action.phrases];
        case GET_LEARNED_PHRASES:
            console.log(action)
            return [...state, action.phrases]
        case CREATE_PHRASE:
            return [...state, action.phrase];
        case UPDATE_PHRASE:
            return state.map((phrase) => phrase.id === action.phrase_id ? action.phrase : phrase);
        case DELETE_PHRASE:
            return state.filter((phrase => phrase.id !== action.phrase_id))
        default:
            return state
    }
}

export default phraseReducer