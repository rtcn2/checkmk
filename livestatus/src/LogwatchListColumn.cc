// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "LogwatchListColumn.h"

#include <algorithm>
#include <iterator>

#include "Column.h"
#include "Logger.h"
#include "MonitoringCore.h"
#include "Row.h"
#include "pnp4nagios.h"

#ifdef CMC
#include "Host.h"
#else
#include "nagios.h"
#endif

std::vector<std::string> LogwatchListColumn::getValue(
    Row row, const contact * /*auth_user*/,
    std::chrono::seconds /*timezone_offset*/) const {
    return getValueImpl(getDirectory(getHostName(row)), *this);
}

std::vector<std::string> LogwatchListColumn::getValueImpl(
    const std::filesystem::path &dir, const Column &col) {
    if (dir.empty()) {
        return {};
    }
    try {
        if (std::filesystem::exists(dir)) {
            std::vector<std::string> filenames;
            auto it = std::filesystem::directory_iterator(dir);
            std::transform(begin(it), end(it), std::back_inserter(filenames),
                           [](const auto &entry) {
                               return entry.path().filename().string();
                           });
            return filenames;
        }
    } catch (const std::filesystem::filesystem_error &e) {
        Warning(col.logger()) << col.name() << ": " << e.what();
    }
    return {};
}

std::filesystem::path LogwatchListColumn::getDirectory(
    const std::string &host_name) const {
    auto logwatch_path = _mc->mkLogwatchPath();
    return logwatch_path.empty() || host_name.empty()
               ? std::filesystem::path()
               : std::filesystem::path(logwatch_path) / pnp_cleanup(host_name);
}

std::string LogwatchListColumn::getHostName(Row row) const {
#ifdef CMC
    if (const auto *hst = columnData<Host>(row)) {
        return hst->name();
    }
#else
    if (const auto *hst = columnData<host>(row)) {
        return hst->name;
    }
#endif
    return "";
}
