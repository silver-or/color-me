import { ArticleController } from "@/modules/controllers/ArticleController";
import { call, put, takeEvery, takeLatest } from "redux-saga/effects";
import { ArticleActions } from "../slices/articleSlice";
import { Article } from "../types";

//get Saga
function* readBestColorsSaga(action: { payload: Article }) {
  const { readBestColorsSuccess, readBestColorsFailure } = ArticleActions;
  const param = action.payload;
  const articleController = new ArticleController();
  try {
    yield call(articleController.readBestColors);
    yield put(readBestColorsSuccess());
  } catch (error) {
    yield put(readBestColorsFailure());
  }
}

function* readHairsSaga(action: { payload: Article }) {
  const { readHairsSuccess, readHairsFailure } = ArticleActions;
  const param = action.payload;
  const articleController = new ArticleController();
  try {
    yield call(articleController.readHairs);
    yield put(readHairsSuccess());
  } catch (error) {
    yield put(readHairsFailure());
  }
}

function* readLipsSaga(action: { payload: Article }) {
  const { readLipsSuccess, readLipsFailure } = ArticleActions;
  const param = action.payload;
  const articleController = new ArticleController();
  try {
    yield call(articleController.readLips);
    yield put(readLipsSuccess());
  } catch (error) {
    yield put(readLipsFailure());
  }
}

function* readPersonalColorsSaga(action: { payload: Article }) {
  const { readPersonalColorsSuccess, readPersonalColorsFailure } = ArticleActions;
  const param = action.payload;
  const articleController = new ArticleController();
  try {
    yield call(articleController.readPersonalColors);
    yield put(readPersonalColorsSuccess());
  } catch (error) {
    yield put(readPersonalColorsFailure());
  }
}

function* readPostsSaga(action: { payload: Article }) {
  const { readPostsSuccess, readPostsFailure } = ArticleActions;
  const param = action.payload;
  const articleController = new ArticleController();
  try {
    yield call(articleController.readPosts);
    yield put(readPostsSuccess());
  } catch (error) {
    yield put(readPostsFailure());
  }
}

function* readSkinsSaga(action: { payload: Article }) {
  const { readSkinsSuccess, readSkinsFailure } = ArticleActions;
  const param = action.payload;
  const articleController = new ArticleController();
  try {
    yield call(articleController.readSkins);
    yield put(readSkinsSuccess());
  } catch (error) {
    yield put(readSkinsFailure());
  }
}

function* readWorstColorsSaga(action: { payload: Article }) {
  const { readWorstColorsSuccess, readWorstColorsFailure } = ArticleActions;
  const param = action.payload;
  const articleController = new ArticleController();
  try {
    yield call(articleController.readWorstColors);
    yield put(readWorstColorsSuccess());
  } catch (error) {
    yield put(readWorstColorsFailure());
  }
}

function* readYoutubersSaga(action: { payload: Article }) {
  const { readYoutubersSuccess, readYoutubersFailure } = ArticleActions;
  const param = action.payload;
  const articleController = new ArticleController();
  try {
    yield call(articleController.readYoutubers);
    yield put(readYoutubersSuccess());
  } catch (error) {
    yield put(readYoutubersFailure());
  }
}

/*
function* fetchMyArticleSaga(action: { payload: any }) {
  const { fetchMyArticleSuccess, fetchMyArticleFailure } = ArticleActions;
  try {
    const response: Article = yield call(action.payload);
    yield put(fetchMyArticleSuccess(response));
  } catch (error) {
    yield put(fetchMyArticleFailure());
  }
}

function* removeArticleSaga(action: { payload: Article }) {
  const articleController = new ArticleController();
  try {
    yield call(articleController.removeArticle, action.payload.id);
  } catch (error) {}
}

function* writeCommentSaga(action: { payload: Article }) {
  const articleController = new ArticleController();
  try {
    yield call(articleController.writeComment, action.payload);
  } catch (error) {}
}
*/


// main saga
export function* watchReadBestColors() {
  yield takeLatest(ArticleActions.writeArticle, readBestColorsSaga);
}

export function* watchReadHairs() {
  yield takeLatest(ArticleActions.writeArticle, readHairsSaga);
}

export function* watchReadLips() {
  yield takeLatest(ArticleActions.writeArticle, readLipsSaga);
}

export function* watchReadPersonalColors() {
  yield takeLatest(ArticleActions.writeArticle, readPersonalColorsSaga);
}

export function* watchReadPosts() {
  yield takeLatest(ArticleActions.writeArticle, readPostsSaga);
}

export function* watchReadSkins() {
  yield takeLatest(ArticleActions.writeArticle, readSkinsSaga);
}

export function* watchReadWorstColors() {
  yield takeLatest(ArticleActions.writeArticle, readWorstColorsSaga);
}

export function* watchReadYoutubers() {
  yield takeLatest(ArticleActions.writeArticle, readYoutubersSaga);
}





/*
export function* watchFetchMyArticleSaga() {
  yield takeEvery(ArticleActions.fetchMyArticle, fetchMyArticleSaga);
}
export function* watchRemoveArticle() {
  yield takeLatest(ArticleActions.removeArticle, removeArticleSaga);
}
export function* watchWriteComment() {
  yield takeLatest(ArticleActions.writeComment, wrtieCommentSaga);
}
*/
