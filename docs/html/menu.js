/*
 @licstart  The following is the entire license notice for the
 JavaScript code in this file.

 Copyright (C) 1997-2017 by Dimitri van Heesch

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License along
 with this program; if not, write to the Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

 @licend  The above is the entire license notice
 for the JavaScript code in this file
 */
function initMenu(relPath,searchEnabled,serverSide,searchPage,search) {
  function makeTree(data,relPath) {
    var result='';
    if ('children' in data) {
      result+='<ul>';
      for (var i in data.children) {
<<<<<<< HEAD
        var url;
        var link;
        link = data.children[i].url;
        if (link.substring(0,1)=='^') {
          url = link.substring(1);
        } else {
          url = relPath+link;
        }
        result+='<li><a href="'+url+'">'+
=======
        result+='<li><a href="'+relPath+data.children[i].url+'">'+
>>>>>>> fe1d33e (doxygen files)
                                data.children[i].text+'</a>'+
                                makeTree(data.children[i],relPath)+'</li>';
      }
      result+='</ul>';
    }
    return result;
  }
<<<<<<< HEAD
<<<<<<< HEAD
  var searchBoxHtml;
  if (searchEnabled) {
    if (serverSide) {
      searchBoxHtml='<div id="MSearchBox" class="MSearchBoxInactive">'+
                 '<div class="left">'+
                  '<form id="FSearchBox" action="'+relPath+searchPage+
                    '" method="get"><span id="MSearchSelectExt">&#160;</span>'+
                  '<input type="text" id="MSearchField" name="query" value="" placeholder="'+search+
                    '" size="20" accesskey="S" onfocus="searchBox.OnSearchFieldFocus(true)"'+
                    ' onblur="searchBox.OnSearchFieldFocus(false)"/>'+
=======
  var searchBox;
  if (searchEnabled) {
    if (serverSide) {
      searchBox='<div id="MSearchBox" class="MSearchBoxInactive">'+
                 '<div class="left">'+
                  '<form id="FSearchBox" action="'+relPath+searchPage+
                    '" method="get"><img id="MSearchSelect" src="'+
                    relPath+'search/mag.svg" alt=""/>'+
                  '<input type="text" id="MSearchField" name="query" value="'+search+
                    '" size="20" accesskey="S" onfocus="searchBox.OnSearchFieldFocus(true)"'+
                    ' onblur="searchBox.OnSearchFieldFocus(false)">'+
>>>>>>> fe1d33e (doxygen files)
                  '</form>'+
                 '</div>'+
                 '<div class="right"></div>'+
                '</div>';
    } else {
<<<<<<< HEAD
      searchBoxHtml='<div id="MSearchBox" class="MSearchBoxInactive">'+
                 '<span class="left">'+
                  '<span id="MSearchSelect" onmouseover="return searchBox.OnSearchSelectShow()"'+
                     ' onmouseout="return searchBox.OnSearchSelectHide()">&#160;</span>'+
                  '<input type="text" id="MSearchField" value="" placeholder="'+search+
=======
      searchBox='<div id="MSearchBox" class="MSearchBoxInactive">'+
                 '<span class="left">'+
                  '<img id="MSearchSelect" src="'+relPath+
                     'search/mag_sel.svg" onmouseover="return searchBox.OnSearchSelectShow()"'+
                     ' onmouseout="return searchBox.OnSearchSelectHide()" alt=""/>'+
                  '<input type="text" id="MSearchField" value="'+search+
>>>>>>> fe1d33e (doxygen files)
                    '" accesskey="S" onfocus="searchBox.OnSearchFieldFocus(true)" '+
                    'onblur="searchBox.OnSearchFieldFocus(false)" '+
                    'onkeyup="searchBox.OnSearchFieldChange(event)"/>'+
                 '</span>'+
                 '<span class="right"><a id="MSearchClose" '+
                  'href="javascript:searchBox.CloseResultsWindow()">'+
                  '<img id="MSearchCloseImg" border="0" src="'+relPath+
<<<<<<< HEAD
                  'search/close.svg" alt=""/></a>'+
                 '</span>'+
=======
                  'search/close.svg" alt=""/></a>'
                 '</span>'
>>>>>>> fe1d33e (doxygen files)
                '</div>';
    }
  }
=======
>>>>>>> 1e8b0f9 ((#57)(#58) Update sphinx path)

  $('#main-nav').append(makeTree(menudata,relPath));
  $('#main-nav').children(':first').addClass('sm sm-dox').attr('id','main-menu');
<<<<<<< HEAD
<<<<<<< HEAD
  if (searchBoxHtml) {
=======
  if (searchBox) {
>>>>>>> fe1d33e (doxygen files)
    $('#main-menu').append('<li id="searchBoxPos2" style="float:right"></li>');
  }
  var $mainMenuState = $('#main-menu-state');
  var prevWidth = 0;
  if ($mainMenuState.length) {
    function initResizableIfExists() {
      if (typeof initResizable==='function') initResizable();
    }
    // animate mobile menu
    $mainMenuState.change(function(e) {
      var $menu = $('#main-menu');
      var options = { duration: 250, step: initResizableIfExists };
      if (this.checked) {
        options['complete'] = function() { $menu.css('display', 'block') };
        $menu.hide().slideDown(options);
      } else {
        options['complete'] = function() { $menu.css('display', 'none') };
        $menu.show().slideUp(options);
      }
    });
    // set default menu visibility
    function resetState() {
      var $menu = $('#main-menu');
      var $mainMenuState = $('#main-menu-state');
      var newWidth = $(window).outerWidth();
      if (newWidth!=prevWidth) {
        if ($(window).outerWidth()<768) {
          $mainMenuState.prop('checked',false); $menu.hide();
<<<<<<< HEAD
          $('#searchBoxPos1').html(searchBoxHtml);
=======
          $('#searchBoxPos1').html(searchBox);
>>>>>>> fe1d33e (doxygen files)
          $('#searchBoxPos2').hide();
        } else {
          $menu.show();
          $('#searchBoxPos1').empty();
<<<<<<< HEAD
          $('#searchBoxPos2').html(searchBoxHtml);
          $('#searchBoxPos2').show();
        }
        if (typeof searchBox!=='undefined') {
          searchBox.CloseResultsWindow();
        }
=======
          $('#searchBoxPos2').html(searchBox);
          $('#searchBoxPos2').show();
        }
>>>>>>> fe1d33e (doxygen files)
        prevWidth = newWidth;
      }
    }
    $(window).ready(function() { resetState(); initResizableIfExists(); });
    $(window).resize(resetState);
=======
  if (searchEnabled) {
    if (serverSide) {
      $('#main-menu').append('<li style="float:right"><div id="MSearchBox" class="MSearchBoxInactive"><div class="left"><form id="FSearchBox" action="'+relPath+searchPage+'" method="get"><img id="MSearchSelect" src="'+relPath+'search/mag.png" alt=""/><input type="text" id="MSearchField" name="query" value="'+search+'" size="20" accesskey="S" onfocus="searchBox.OnSearchFieldFocus(true)" onblur="searchBox.OnSearchFieldFocus(false)"></form></div><div class="right"></div></div></li>');
    } else {
      $('#main-menu').append('<li style="float:right"><div id="MSearchBox" class="MSearchBoxInactive"><span class="left"><img id="MSearchSelect" src="'+relPath+'search/mag_sel.png" onmouseover="return searchBox.OnSearchSelectShow()" onmouseout="return searchBox.OnSearchSelectHide()" alt=""/><input type="text" id="MSearchField" value="'+search+'" accesskey="S" onfocus="searchBox.OnSearchFieldFocus(true)" onblur="searchBox.OnSearchFieldFocus(false)" onkeyup="searchBox.OnSearchFieldChange(event)"/></span><span class="right"><a id="MSearchClose" href="javascript:searchBox.CloseResultsWindow()"><img id="MSearchCloseImg" border="0" src="'+relPath+'search/close.png" alt=""/></a></span></div></li>');
    }
>>>>>>> 1e8b0f9 ((#57)(#58) Update sphinx path)
  }
  $('#main-menu').smartmenus();
}
/* @license-end */
