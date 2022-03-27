"""Test how SVG shapes are transformed."""

from ...testing_utils import assert_no_logs
from .. import assert_pixels


@assert_no_logs
def test_transform_translate():
    assert_pixels('transform_translate', 9, 9, '''
        _________
        _RRRRRRR_
        _RRRRRRR_
        _RR___RR_
        _RR___RR_
        _RR___RR_
        _RRRRRRR_
        _RRRRRRR_
        _________
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect x="0" y="4" width="5" height="5" transform="translate(2, -2)"
              stroke-width="2" stroke="red" fill="none" />
      </svg>
    ''')


@assert_no_logs
def test_transform_translatex():
    assert_pixels('transform_translatex', 9, 9, '''
        _________
        _RRRRRRR_
        _RRRRRRR_
        _RR___RR_
        _RR___RR_
        _RR___RR_
        _RRRRRRR_
        _RRRRRRR_
        _________
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect x="0" y="2" width="5" height="5" transform="translateX(2)"
              stroke-width="2" stroke="red" fill="none" />
      </svg>
    ''')


@assert_no_logs
def test_transform_translatey():
    assert_pixels('transform_translatey', 9, 9, '''
        _________
        _RRRRRRR_
        _RRRRRRR_
        _RR___RR_
        _RR___RR_
        _RR___RR_
        _RRRRRRR_
        _RRRRRRR_
        _________
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect x="2" y="0" width="5" height="5" transform="translateY(2)"
              stroke-width="2" stroke="red" fill="none" />
      </svg>
    ''')


@assert_no_logs
def test_transform_rotate():
    assert_pixels('transform_rotate', 9, 9, '''
        _________
        _RRRRRRR_
        _RRRRRRR_
        _RR___RR_
        _RR___RR_
        _RRRRRRR_
        _RRRRRRR_
        _________
        _________
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect x="2" y="-7" width="4" height="5" transform="rotate(90)"
              stroke-width="2" stroke="red" fill="none" />
      </svg>
    ''')


@assert_no_logs
def test_transform_rotate_cx_cy():
    assert_pixels('transform_rotate_cx_cy', 9, 9, '''
        _________
        _RRRRRRR_
        _RRRRRRR_
        _RR___RR_
        _RR___RR_
        _RRRRRRR_
        _RRRRRRR_
        _________
        _________
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect x="7" y="2" width="4" height="5" transform="rotate(90 7 2)"
              stroke-width="2" stroke="red" fill="none" />
      </svg>
    ''')


@assert_no_logs
def test_transform_skew():
    assert_pixels('transform_skew', 9, 9, '''
        _________
        _RRR_____
        _RRRRRR__
        __RRRRR__
        __RRRRR__
        __RRRRRR_
        ____RRRR_
        _________
        _________
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect x="2" y="2" width="2" height="2" transform="skew(20 20)"
              stroke-width="2" stroke="red" fill="none" />
      </svg>
    ''')


@assert_no_logs
def test_transform_skewx():
    assert_pixels('transform_skewx', 9, 9, '''
        _________
        _RRRRR___
        _RRRRRR__
        __RRRRR__
        __RRRRR__
        _________
        _________
        _________
        _________
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect x="2" y="2" width="2" height="2" transform="skewX(20)"
              stroke-width="2" stroke="red" fill="none" />
      </svg>
    ''')


@assert_no_logs
def test_transform_skewy():
    assert_pixels('transform_skewy', 9, 9, '''
        _________
        _RR______
        _RRRR____
        _RRRR____
        _RRRR____
        _RRRR____
        __RRR____
        _________
        _________
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect x="2" y="2" width="2" height="2" transform="skewY(20)"
              stroke-width="2" stroke="red" fill="none" />
      </svg>
    ''')


@assert_no_logs
def test_transform_scale():
    assert_pixels('transform_scale', 9, 9, '''
        _________
        _RRRRRRR_
        _RRRRRRR_
        _RRRRRRR_
        _RRRRRRR_
        _RRRRRRR_
        _RRRRRRR_
        _RRRRRRR_
        _________
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect x="2" y="2" width="2" height="2" transform="scale(1.5)"
              stroke-width="2" stroke="red" fill="none" />
      </svg>
    ''')


@assert_no_logs
def test_transform_scale_2():
    assert_pixels('transform_scale_2', 9, 9, '''
        _________
        _RRRRRRR_
        _RRRRRRR_
        _RRRRRRR_
        _RRRRRRR_
        _RRRRRRR_
        _RRRRRRR_
        _RRRRRRR_
        _________
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect x="2" y="2" width="2" height="2" transform="scale(1.5 1.5)"
              stroke-width="2" stroke="red" fill="none" />
      </svg>
    ''')


@assert_no_logs
def test_transform_scalex():
    assert_pixels('transform_scalex', 9, 9, '''
        _________
        _RRRRRRR_
        _RRRRRRR_
        _RRRRRRR_
        _RRRRRRR_
        _________
        _________
        _________
        _________
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect x="2" y="2" width="2" height="2" transform="scaleX(1.5)"
              stroke-width="2" stroke="red" fill="none" />
      </svg>
    ''')


@assert_no_logs
def test_transform_scaley():
    assert_pixels('transform_scaley', 9, 9, '''
        _________
        _RRRR____
        _RRRR____
        _RRRR____
        _RRRR____
        _RRRR____
        _RRRR____
        _RRRR____
        _________
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect x="2" y="2" width="2" height="2" transform="scaleY(1.5)"
              stroke-width="2" stroke="red" fill="none" />
      </svg>
    ''')


@assert_no_logs
def test_transform_matrix():
    assert_pixels('transform_matrix', 9, 9, '''
        _________
        _RRRRRRR_
        _RRRRRRR_
        _RRRRRRR_
        _RRRRRRR_
        _RRRRRRR_
        _RRRRRRR_
        _RRRRRRR_
        _________
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect x="0" y="0" width="2" height="2"
              transform="matrix(1.5 0 0 1.5 3 3)"
              stroke-width="2" stroke="red" fill="none" />
      </svg>
    ''')


@assert_no_logs
def test_transform_multiple():
    assert_pixels('transform_multiple', 9, 9, '''
        _________
        _RRRRRRR_
        _RRRRRRR_
        _RR___RR_
        _RR___RR_
        _RRRRRRR_
        _RRRRRRR_
        _________
        _________
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect x="0" y="0" width="4" height="5"
              transform="rotate(90) translateY(-7) translateX(2)"
              stroke-width="2" stroke="red" fill="none" />
      </svg>
    ''')
