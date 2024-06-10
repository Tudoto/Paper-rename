chrome.downloads.onDeterminingFilename.addListener((downloadItem, suggest) => {
    // 检查是否需要修改文件名
      // 修改文件名
      const newName = 'modified_file.pdf';
      suggest({filename: newName, conflictAction: "overwrite"});
  });
  
  
