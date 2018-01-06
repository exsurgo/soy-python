import java.util.*;
import com.google.common.collect.ImmutableSet;
import com.google.template.soy.pysrc.restricted.SoyPySrcFunction;
import com.google.template.soy.pysrc.restricted.PyExpr;

/**
 * Provides a function for calling a python method dynamically.
 */
public class CallMethodFunction implements SoyPySrcFunction {

    public PyExpr computeForPySrc(List<PyExpr> args) {
        String code = "getattr((__import__(data['module'])), data['method'])()";
        return new PyExpr(code, Integer.MAX_VALUE);
    }

    public String getName() {
        return "callMethod";
    }

    public Set<Integer> getValidArgsSizes() {
        return ImmutableSet.of(2);
    }

}
