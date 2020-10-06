#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#include <dirent.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <errno.h>

using std::cout;
using std::string;
using std::vector;
using std::endl;
using std::ifstream;

void printDirectoryStructure(string dir, string prefix, vector<string>& ignore) {
  string filepath;
  DIR *dp;
  struct dirent *dirp;
  struct stat filestat;

  /**
   * Open current directory
   */
  dp = opendir(dir.c_str());
  
  /**
   * Error check & base case
   */
  if (dp == NULL) {
    cout << "Error " << errno << " while trying opening" << dir << endl;
    return;
  }

  /**
   * Read all files and folders in current directory
   */
  while (dirp = readdir(dp)) {
    
    /* Setup file path string, i.e. "Git/cpp/folder1/file.txt" */
    filepath = dir + "/" + dirp->d_name;
    
    /* Will only get the file.txt in the above string */
    string nameString(dirp->d_name);
    
    /* If either the filepath or the nameString exist in the ignore vector, do not print them */
    if(std::find(ignore.begin(), ignore.end(), nameString) != ignore.end() || std::find(ignore.begin(), ignore.end(), filepath) != ignore.end()) {
      continue;
    } else {
      string tmpprefix = prefix;
      tmpprefix.replace(tmpprefix.size()-3, 3, "├─");
      cout << tmpprefix << dirp->d_name << endl;
    }

    /**
     * Upon successful completion, 0 shall be returned. Otherwise, -1 shall be returned and errno set to indicate the error.
     * http://pubs.opengroup.org/onlinepubs/009695399/functions/stat.html
     */
    if (stat(filepath.c_str(), &filestat)) {
      continue;
    }
    
    /**
     * If we're viewing a directory, recurse through its contents (DFS)
     */
    if (S_ISDIR(filestat.st_mode)) {
      printDirectoryStructure(filepath, prefix + "   │", ignore);
    }
  
  }
  closedir(dp);
}

vector<string> buildIgnoreVector() {
  vector<string> ignore;
  /* Ignore the following file and folder names */
  ignore.push_back(".");
  ignore.push_back("..");
  ignore.push_back("node_modules");
  ignore.push_back("bower_components");
  ignore.push_back(".git");
  return ignore;

}

int main(int argc, char *argv[]) {
  if (!argv[1]) {
    cout << "You must type a directory name" << endl;
    return -1;
  }
  string dir(argv[1]);
  vector<string> ignore = buildIgnoreVector();
  /**
   * As command line arguments, pass any file or directory name you wish to ignore after the directory you wish to view
   */
  for (int i = 2; i < argc; ++i) {
    ignore.push_back(string(argv[i]));
  }
  
  cout << "." << endl;
  printDirectoryStructure(dir, "│", ignore);
  cout << endl << "Dom Farolino\ndomfarolino.com\n<domfarolino@gmail.com>\n<cpuxtech@gmail.com>\n";
  return 0;
}