# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

from lizard_map.views import AppView
from lizard_area.models import Area
from lizard_history.utils import get_history
from lizard_history.utils import get_specific_history

import lizard_wbconfiguration

WBCONFIGURATION_MODELS = (
    lizard_wbconfiguration.models.AreaConfiguration,
    lizard_wbconfiguration.models.Structure,
    lizard_wbconfiguration.models.Bucket,
)


def area_structures(area_code):
    pass


def area_buckets(area_code):
    pass


class WBConfigurationHistoryView(AppView):
    """
    Show waterbalanceconfiguration history
    """
    template_name='lizard_wbconfiguration/wbconfiguration_history.html'

    def area(self):
        """
        Return an area.
        """
        if not hasattr(self, '_area'):
            self._area = Area.objects.get(
                ident=self.area_ident)
        return self._area

    def history(self):
        """
        Return history.
        """
        if not hasattr(self, '_history'):
            self._history = get_specific_history(
                WBCONFIGURATION_MODELS,
                self.area(),
            )
        return self._history
    
    def get(self, request, *args, **kwargs):
        self.area_ident = request.GET.get('object_id')
        return super(WBConfigurationHistoryView, self).get(
            request, *args, **kwargs)


class WBConfigurationArchiveView(AppView):
    """
    Readonly esf tree.
    """
    def history(self):
        """
        Return history.
        """
        if not hasattr(self, '_history'):
            self._history = get_history(
                log_entry_id=self.log_entry_id,
                include_data=False,
            )
        return self._history
    
    def area(self):
        """
        Return an area.
        """
        if not hasattr(self, '_area'):
            self._area = Area.objects.get(
                ident=self.area_ident)
        return self._area

    def get(self, request, *args, **kwargs):
        """
        Return read only form for esf configuration corresponding to
        specific log_entry.
        """
        if request.user.is_authenticated():
            self.template_name = 'lizard_wbconfiguration/wbconfiguration_read_only.js'
            self.log_entry_id = kwargs.get('log_entry_id')
            # For the special case of esf trees, the area_ident is
            # stored in the object_repr field of the log_entry.
            self.area_ident = self.history()['object_repr']
        else:
            self.template_name = 'portals/geen_toegang.js'
        return super(
            WBConfigurationArchiveView,
            self
        ).get(request, *args, **kwargs)


