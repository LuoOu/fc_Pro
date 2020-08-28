/****************************************************************************
**
** Copyright (C) 2016 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of PySide2.
**
** $QT_BEGIN_LICENSE:LGPL$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPL3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 2.0 or (at your option) the GNU General
** Public license version 3 or any later version approved by the KDE Free
** Qt Foundation. The licenses are as published by the Free Software
** Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
** included in the packaging of this file. Please review the following
** information to ensure the GNU General Public License requirements will
** be met: https://www.gnu.org/licenses/gpl-2.0.html and
** https://www.gnu.org/licenses/gpl-3.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/


#ifndef SBK_QTWEBENGINECORE_PYTHON_H
#define SBK_QTWEBENGINECORE_PYTHON_H

#include <sbkpython.h>
#include <sbkconverter.h>
#include <sbkenum.h>
#include <basewrapper.h>
#include <bindingmanager.h>
#include <memory>

#include <pysidesignal.h>
// Module Includes
#include <pyside2_qtcore_python.h>

// Binded library includes
#include <qwebengineurlschemehandler.h>
#include <qwebenginehttprequest.h>
#include <qwebengineurlrequestinterceptor.h>
#include <qwebengineurlrequestjob.h>
#include <qwebengineurlrequestinfo.h>
#include <qwebenginecookiestore.h>
// Conversion Includes - Primitive Types
#include <signalmanager.h>
#include <qabstractitemmodel.h>
#include <QStringList>
#include <wtypes.h>
#include <QString>

// Conversion Includes - Container Types
#include <QMap>
#include <QMultiMap>
#include <QVector>
#include <QList>
#include <pysideqflags.h>
#include <QPair>
#include <QSet>
#include <QQueue>
#include <QLinkedList>
#include <QStack>

// Type indices
#define SBK_QWEBENGINEURLREQUESTINFO_IDX                             3
#define SBK_QWEBENGINEURLREQUESTINFO_RESOURCETYPE_IDX                5
#define SBK_QWEBENGINEURLREQUESTINFO_NAVIGATIONTYPE_IDX              4
#define SBK_QWEBENGINEURLREQUESTINTERCEPTOR_IDX                      6
#define SBK_QWEBENGINECOOKIESTORE_IDX                                0
#define SBK_QWEBENGINEURLREQUESTJOB_IDX                              7
#define SBK_QWEBENGINEURLREQUESTJOB_ERROR_IDX                        8
#define SBK_QWEBENGINEURLSCHEMEHANDLER_IDX                           9
#define SBK_QWEBENGINEHTTPREQUEST_IDX                                1
#define SBK_QWEBENGINEHTTPREQUEST_METHOD_IDX                         2
#define SBK_QtWebEngineCore_IDX_COUNT                                10

// This variable stores all Python types exported by this module.
extern PyTypeObject** SbkPySide2_QtWebEngineCoreTypes;

// This variable stores all type converters exported by this module.
extern SbkConverter** SbkPySide2_QtWebEngineCoreTypeConverters;

// Converter indices
#define SBK_QTWEBENGINECORE_QLIST_QOBJECTPTR_IDX                     0 // const QList<QObject* > &
#define SBK_QTWEBENGINECORE_QLIST_QBYTEARRAY_IDX                     1 // QList<QByteArray >
#define SBK_QTWEBENGINECORE_QVECTOR_QBYTEARRAY_IDX                   2 // QVector<QByteArray >
#define SBK_QTWEBENGINECORE_QMAP_QSTRING_QSTRING_IDX                 3 // const QMap<QString,QString > &
#define SBK_QTWEBENGINECORE_QLIST_QVARIANT_IDX                       4 // QList<QVariant >
#define SBK_QTWEBENGINECORE_QLIST_QSTRING_IDX                        5 // QList<QString >
#define SBK_QTWEBENGINECORE_QMAP_QSTRING_QVARIANT_IDX                6 // QMap<QString,QVariant >
#define SBK_QtWebEngineCore_CONVERTERS_IDX_COUNT                     7

// Macros for type check

namespace Shiboken
{

// PyType functions, to get the PyObjectType for a type T
template<> inline PyTypeObject* SbkType< ::QWebEngineUrlRequestInfo::ResourceType >() { return SbkPySide2_QtWebEngineCoreTypes[SBK_QWEBENGINEURLREQUESTINFO_RESOURCETYPE_IDX]; }
template<> inline PyTypeObject* SbkType< ::QWebEngineUrlRequestInfo::NavigationType >() { return SbkPySide2_QtWebEngineCoreTypes[SBK_QWEBENGINEURLREQUESTINFO_NAVIGATIONTYPE_IDX]; }
template<> inline PyTypeObject* SbkType< ::QWebEngineUrlRequestInfo >() { return reinterpret_cast<PyTypeObject*>(SbkPySide2_QtWebEngineCoreTypes[SBK_QWEBENGINEURLREQUESTINFO_IDX]); }
template<> inline PyTypeObject* SbkType< ::QWebEngineUrlRequestInterceptor >() { return reinterpret_cast<PyTypeObject*>(SbkPySide2_QtWebEngineCoreTypes[SBK_QWEBENGINEURLREQUESTINTERCEPTOR_IDX]); }
template<> inline PyTypeObject* SbkType< ::QWebEngineCookieStore >() { return reinterpret_cast<PyTypeObject*>(SbkPySide2_QtWebEngineCoreTypes[SBK_QWEBENGINECOOKIESTORE_IDX]); }
template<> inline PyTypeObject* SbkType< ::QWebEngineUrlRequestJob::Error >() { return SbkPySide2_QtWebEngineCoreTypes[SBK_QWEBENGINEURLREQUESTJOB_ERROR_IDX]; }
template<> inline PyTypeObject* SbkType< ::QWebEngineUrlRequestJob >() { return reinterpret_cast<PyTypeObject*>(SbkPySide2_QtWebEngineCoreTypes[SBK_QWEBENGINEURLREQUESTJOB_IDX]); }
template<> inline PyTypeObject* SbkType< ::QWebEngineUrlSchemeHandler >() { return reinterpret_cast<PyTypeObject*>(SbkPySide2_QtWebEngineCoreTypes[SBK_QWEBENGINEURLSCHEMEHANDLER_IDX]); }
template<> inline PyTypeObject* SbkType< ::QWebEngineHttpRequest::Method >() { return SbkPySide2_QtWebEngineCoreTypes[SBK_QWEBENGINEHTTPREQUEST_METHOD_IDX]; }
template<> inline PyTypeObject* SbkType< ::QWebEngineHttpRequest >() { return reinterpret_cast<PyTypeObject*>(SbkPySide2_QtWebEngineCoreTypes[SBK_QWEBENGINEHTTPREQUEST_IDX]); }

} // namespace Shiboken

#endif // SBK_QTWEBENGINECORE_PYTHON_H
