import * as React from 'react';
import * as ReactDOM from 'react-dom';

import { Content } from './Content';
import { GoogleButton } from './GoogleButton';

ReactDOM.render(<Content />, document.getElementById('content'));
ReactDOM.render(<GoogleButton />, document.getElementById('googlebutton'));