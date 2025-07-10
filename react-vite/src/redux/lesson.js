import { csrfFetch } from "./csrf";

// const initialState = {
//     lessons: [],
//     questions: [],
//     result: null,
//     error: null
// };
// const initialState = []

const initialState = {
    entities: {
        lessons: {},
        questions: {},
    },
    allLessonIds: [],
    currentLessonId: null,
    // currentQuestionForLesson: [],
    // result: null,
    error: null

}
export const LOAD_LESSONS = "LOAD_LESSONS";
export const LOAD_LESSON_DETAILS = "LOAD_LESSON_DETAILS";
export const LOAD_QUESTIONS = "LOAD_QUESTIONS";
export const ADD_LESSON = "ADD_LESSON";
export const UPDATE_LESSON = "UPDATE_LESSON";
export const DELETE_LESSON = "DELETE_LESSON";
export const COMPLETE_LESSON = "COMPLETE_LESSON";
export const CLEAR_LESSON_DETAILS = 'CLEAR_LESSON_DETAILS';

export const loadLessons = (lessons) => ({
    type: LOAD_LESSONS,
    lessons
});

export const loadLessonDetails = (lesson) => ({
    type: LOAD_LESSON_DETAILS,
    lesson
});

export const lessonQuestions = (questions, lesson_id) => ({
    type: LOAD_QUESTIONS,
    questions,
    lesson_id
});

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

export const completeLesson = (lesson) => ({
    type: COMPLETE_LESSON,
    lesson
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
};

export const fetchLessonDetails = (lesson_id) => async (dispatch) => {
    const response = await csrfFetch(`/api/lessons/${lesson_id}`);
    if (response.ok) {
        const lesson = await response.json();
        dispatch(loadLessonDetails(lesson)) 
    } else {
        throw new Error('Failed to complete task');
    }
};

export const fetchQuestions = (lesson_id) => async (dispatch) => {
    const response = await csrfFetch(`/api/lessons/${lesson_id}/questions`);
    if (response.ok) {
        const questions = await response.json();
        dispatch(lessonQuestions(questions));
        return questions
    } else {
        throw new Error('No Questions Found')
    }
};

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
};

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
    console.log("Data",lessonData)
    const response = await csrfFetch(`/api/lessons/${lessonData.id}/complete`, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(lessonData)
    });

    if (response.ok) {
        const result = await response.json()
        console.log(result)
        dispatch(completeLesson(result))
        return result
    } else {
        throw new Error('Failed to complete task');
    }
};


const lessonReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOAD_LESSONS:{
            // return [...action.lessons.lessons];
            const newLessons = {};
            action.lessons.lessons.forEach(lesson => {
                newLessons[lesson.id] = lesson;
            });
            return {
                ...state,
                entities: {
                    ...state.entities,
                    lessons: newLessons
                },
                allLessonIds: action.lessons.lessons.map(lesson => lesson.id)
            }
        }
        case LOAD_LESSON_DETAILS:{
            // console.log("ACTION", action)
            // return [...state.filter(lesson => lesson.id !== action.lesson.id), action.lesson]
            const { lesson } = action;
            const newQuestions = {};

            if (lesson.questions && Array.isArray(lesson.questions)) {
                lesson.questions.forEach(question => {
                    newQuestions[question.id] = question;
                });
            }

            return {
                ...state,
                entities: {
                    ...state.entities,
                    lessons: {
                        ...state.entities.lessons,
                        [lesson.id]: {
                            ...lesson,
                            questions: lesson.questions ? lesson.questions.map(q => q.id) : []
                        }
                    },

                    questions: {
                        ...state.entities.questions,
                        ...newQuestions
                    }
                },

                currentLessonId: lesson.id
            }
        }
        case LOAD_QUESTIONS:{
            // return {
            //     ...state,
            //     questions: action.questions
            // };
            const { questions, lesson_id } = action;
            const newQuestions = {};

            questions.questions.forEach(question => {
                newQuestions[question.id] = question
            });

            if (!state.entities.lessons[lesson.id]) {
                return state
            }

            return {
                ...state,
                entities: {
                    ...state.entities,
                    lessons: {
                        ...state.entities,lessons,
                        [lesson_id]: {
                            ...state.entities.lessons[lesson.id],
                            questions: questions.questions.map(q => q.id)
                        }
                    },
                    questions : {
                        ...state.entities,questions,
                        ...newQuestions
                    }
                }
            }
        }

        case CLEAR_LESSON_DETAILS:
            // return initialState
            return {
                ...state,
                currentLessonId: null
            };
        case ADD_LESSON: {
            // return [...state, action.lesson];
            const { lesson } = action;
            return {
                ...state,
                entities: {
                    ...state.entities,
                    lessons : {
                        ...state.entities.lessons,
                        [lesson.id]: lesson
                    }
                },
                allLessonIds: [...state.allLessonIds, lesson.id]
            }
        }
        case UPDATE_LESSON:
            // return state.map((lesson) => lesson.id === action.lesson_id ? action.lesson : lesson)
        case COMPLETE_LESSON:{
            const { lesson } = action;
            return {
                ...state,
                entities : {
                    ...state.entities.lessons,
                    [lesson.id]: lesson
                }
            };
        }
            // return state
        case DELETE_LESSON:{
            const { lesson_id } = action;
            const newLessons = {...state.entities.lessons};
            delete newLessons[lesson.id];

            return {
                ...state,
                entities: {
                    ...state.entities,
                    lessons: newLessons
                },
                allLessonIds: state.allLessonIds.filter(id => id !== lesson_id)
            }
        }
            // return state.filter(lesson => lesson.id !== action.lesson)
        default:
            return state;
    }
}

export default lessonReducer
