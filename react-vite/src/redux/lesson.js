import { csrfFetch } from "./csrf";

const initialState = []

export const LOAD_LESSONS = "LOAD_LESSONS";
export const LOAD_LESSON_DETAILS = "LOAD_LESSON_DETAILS";
export const ADD_LESSON = "ADD_LESSON";
export const UPDATE_LESSON = "UPDATE_LESSON";
export const DELETE_LESSON = "DELETE_LESSON";
export const COMPLETE_LESSON = "COMPLETE_LESSON";
export const CLEAR_LESSON_DETAILS = 'CLEAR_LESSON_DETAILS'

export const loadLessons = (lessons) => ({
    type: LOAD_LESSONS,
    lessons
});
export const loadLessonDetails = (lesson) => ({
    type: LOAD_LESSON_DETAILS,
    lesson
})

export const clearLessonDetails = () => ({
    type: CLEAR_LESSON_DETAILS
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
        const lessons = await response.json();
        dispatch(loadLessons(lessons))
        return lessons
    } else {
        const errorData = await response.json()
        console.error("ERROR", errorData )
        throw new Error('Failed to complete task');
    }
}

export const fetchLessonDetails = (lesson_id) => async (dispatch) => {
    const response = await csrfFetch(`/api/lessons/${lesson_id}`);
    if (response.ok) {
        const lesson = await response.json();
        dispatch(loadLessonDetails(lesson)) 
    } else {
        throw new Error('Failed to complete task');
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
    } else {
        throw new Error('Failed to complete task');
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
    } else {
        throw new Error('Failed to complete task');
    }
};

export const removeLesson = (lesson_id) => async (dispatch) => {
    const response = await csrfFetch(`/api/lessons/${lesson_id}`, {
        method: 'DELETE'
    });
    if (response.ok) {
        dispatch(deleteLesson(lesson_id))
    } else {
        throw new Error('Failed to complete task');
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
    } else {
        throw new Error('Failed to complete task');
    }
};


const lessonReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_LESSONS:
            return [...action.lessons.lessons];
        case LOAD_LESSON_DETAILS:
            console.log("ACTION", action)
            return [...state.filter(lesson => lesson.id !== action.lesson.id), action.lesson]
        case CLEAR_LESSON_DETAILS:
            return initialState
        case ADD_LESSON:
            return [...state, action.lesson];
        case UPDATE_LESSON:
            return state.map((lesson) => lesson.id === action.lesson_id ? action.lesson : lesson)
        case DELETE_LESSON:
            return state.filter(lesson => lesson.id !== action.lesson)
        case COMPLETE_LESSON:
            return state
        default:
            return state;
    }
}

export default lessonReducer
