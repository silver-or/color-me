import "bootstrap/dist/css/bootstrap.css";
import React, { useState } from "react";
import Link from "next/link";
import { HOST_3001 } from "@/components/common/Path";

const Nav: React.FC = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light">
   
      <div className="container-fluid">
        <Link href="/">
          <a className="navbar-brand">
            <img
              src="https://ifh.cc/g/4vnqom.png"
              style={{ width: 110 + "px" }}
              alt="logo"
            />
          </a>
        </Link>

        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0 m-auto">
            <ul className="navbar-nav mr-auto">
              <li className="nav-item active">
                <Link href="/personal_color/fileUpload">
                  <a className="nav-link">퍼스널컬러 진단 받기</a>
                </Link>
              </li>
            </ul>

            {/* <ul className="navbar-nav mr-auto">
              <li className="nav-item active">
                <Link href="/personal_color/fileUpload">
                  <a className="nav-link">사진 업로드</a>
                </Link>
              </li>
            </ul> */}

            <li className="nav-item dropdown">
              <a
                className="nav-link dropdown-toggle "
                href="#"
                id="navbarDropdown"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                추천
              </a>
              <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
                <li>
                  <Link href="/recommend/youtuber">
                    <a className="dropdown-item">유튜버</a>
                  </Link>
                </li>
                <li>
                  <Link href="/recommend/best_color">
                    <a className="dropdown-item">best color</a>
                  </Link>
                </li>
                <li>
                  <Link href="/recommend/worst_color">
                    <a className="dropdown-item">worst color</a>
                  </Link>
                </li>
                <li>
                  <Link href="/recommend/hair">
                    <a className="dropdown-item">머리 색</a>
                  </Link>
                </li>
                <li>
                  <Link href="/recommend/skin">
                    <a className="dropdown-item">피부 기초</a>
                  </Link>
                </li>
                <li>
                  <Link href="/recommend/lip">
                    <a className="dropdown-item">립</a>
                  </Link>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Nav;
