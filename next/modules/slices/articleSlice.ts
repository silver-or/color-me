import { Article, ArticleState } from "@/modules/types";
import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { ArticleService } from "../services/ArticleService";

const articleService = new ArticleService();
const ArticleSlice = createSlice(articleService.createArticleSlice());

export const {
  writeArticle,
  readBestColorsSuccess,
  readBestColorsFailure,
  readHairsSuccess,
  readHairsFailure,
  readLipsSuccess,
  readLipsFailure,
  readPersonalColorsSuccess,
  readPersonalColorsFailure,
  readPostsSuccess,
  readPostsFailure,
  readSkinsSuccess,
  readSkinsFailure,
  readWorstColorsSuccess,
  readWorstColorsFailure,
  readYoutubersSuccess,
  readYoutubersFailure,
} = ArticleSlice.actions;
const { reducer, actions } = ArticleSlice;
export const ArticleActions = actions;
export default reducer;
