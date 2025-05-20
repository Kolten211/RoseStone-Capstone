import { csrfFetch } from "./csrf"

// const initialState = {
//     translatedText: null
// }

const TRANSLATE_REQUEST = "TRANSLATE_REQUEST"


const translate = (translation) =>({
    type: TRANSLATE_REQUEST,
    translation
})

export const translateText = (text, source_lang, target_lang) => async (dispatch) => {
    const response = await csrfFetch('/api/translate/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text, source_lang, target_lang }),
    })
    if (response.ok) {
        const translation = await response.json();
        console.log("TRANSLATION", translation)
        dispatch(translate(translation))
        return translation
    } 
}

// const translateReducer = (state = initialState, action) => {
//     switch (action.type) {
//         case TRANSLATE_REQUEST:
//             return {
//                 ...state,
//                 translatedText: action.translation.translated_text
//             }
//         default:
//             return state
//     }
// }


export default translateText