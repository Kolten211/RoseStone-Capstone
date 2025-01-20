import { csrfFetch } from "./csrf";

const initialState = []

export const LOAD_LESSONS = "LOAD_LESSONS";
export const ADD_LESSON = "ADD_LESSON";
export const UPDATE_LESSON = "UPDATE_LESSON";
export const DELETE_LESSON = "DELETE_LESSON";
export const COMPLETE_LESSON = "COMPLETE_LESSON";

export const loadLessons = (lessons) => ({
    type: LOAD_LESSONS,
    lessons
});

export const addLesson = (lesson) => ({
    type: ADD_LESSON,
    lesson
});

export const updateLesson = (lesson) => ({
    type: UPDATE_LESSON,
    lesson
});

export const deleteLesson = (lesson_id) => ({
    type: DELETE_LESSON,
    lesson_id
});

export const completeLesson = (lesson_id) => ({
    type: COMPLETE_LESSON,
    lesson_id
});

export const fetchLessons = () => async (dispatch) => {
    const response = await csrfFetch('/api/lessons/');

    if (response.ok) {
        dispatch(loadLessons(response))
    }
}

export const createLesson = (lessonData) => async (dispatch) => {
    const response = await csrfFetch('/api/lessons/create', {
        method:'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(lessonData)
    });

    if (response.ok) {
        const newLesson = await response.json();

        dispatch(addLesson(newLesson));

        return newLesson
    }
}

export const editLesson = (lessonData) => async (dispatch) => {
    const response = await csrfFetch(`/api/lessons/${lessonData.id}`, {
        method:'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(lessonData)
    });

    if (response.ok) {
        const newData = response.json()
        dispatch(updateLesson(newData));

        return newData
    }
};

export const removeLesson = (lesson_id) => async (dispatch) => {
    const response = await csrfFetch(`/api/lessons/${lesson_id}`, {
        method: 'DELETE'
    });
    if (response.ok) {
        dispatch(deleteLesson(lesson_id))
    }
};

export const finishedLesson = (lessonData) => async (dispatch) => {
    const response = await csrfFetch(`/api/lesson/${lessonData.id}/complete`, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(lessonData)
    });

    if (response.ok) {
        dispatch(completeLesson(lessonData))
    }
};


const lessonReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_LESSONS:
            return [...action.lessons];
        case ADD_LESSON:
            return [...state, action.lesson];
        case UPDATE_LESSON:
            return state.map((lesson) => lesson.id === action.lesson_id ? action.leson : lesson)
        case DELETE_LESSON:
            return state.map((lesson) => lesson.id !== action.lesson_id)
        case COMPLETE_LESSON:
            return state
        default:
            return state;
    }
}

export default lessonReducer
